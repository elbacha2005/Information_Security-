import sys
from collections import Counter
from PIL import Image

W, H = 432, 475
data = open(sys.argv[1], 'rb').read()

ct = data[16:16 + W * H]                                  # skip "Salted__" + salt, drop padding block
blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]      # 16-byte AES blocks

count = Counter(blocks)
print(len(blocks), "blocks,", len(count), "unique,", len(blocks) - len(count), "duplicates")

shade = {b: i * 255 // len(count) for i, b in enumerate(count)}   # same block -> same gray
pixels = b''.join(bytes([shade[b]]) * 16 for b in blocks)         # 1 block = 16 pixels

Image.frombytes('L', (W, H), pixels).save(sys.argv[2])