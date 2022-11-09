import wave

string = input ("\nEnter your Message: ")
msg = string
song = wave.open("song.wav", mode='rb')
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
for i, bit in enumerate(bits):
  frame_bytes[i] = (frame_bytes[i] & 254) | bit
frame_modified = bytes(frame_bytes)

with wave.open('do-not-rename.wav', 'wb') as fd:
  fd.setparams(song.getparams())
  fd.writeframes(frame_modified)
song.close()

print(f"Message encoded: {msg}\n")