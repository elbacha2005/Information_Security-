import sys
d = open(sys.argv[1],'rb').read()[16:16+432*475]
b = [d[i:i+16] for i in range(0, len(d), 16)]
print(len(b), 'blocks', len(set(b)), 'unique', len(b)-len(set(b)), 'repeated')