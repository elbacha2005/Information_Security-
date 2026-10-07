from collections import Counter

def caesar(text, k):
    result = ""
    for c in text.upper():
        if c.isalpha():
            result += chr((ord(c) - 65 + k) % 26 + 65)
        else:
            result += c
    return result

def brute_force_caesar(text):
    decrypted_texts = []
    n = len(decrypted_texts)
    for k in range(26):
        decrypted_texts.append(caesar(text, -k))
        
    for i in range(len(decrypted_texts)):
        print(f"Shift {i}:  {decrypted_texts[i]}")



PLAIN  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CIPHER = "QMJZTGFKPWLSBOXNCRYEVHIADU"
 
def sub_encrypt(text):
    result = ""
    for c in text.upper():
        if c in PLAIN:
            i = PLAIN.index(c)
            result += CIPHER[i]
        else:
            result += c
    return result

def sub_decrypt(text):
    result = ""
    for c in text.upper():
        if c in CIPHER:
            i = CIPHER.index(c)
            result += PLAIN[i]
        else:
            result += c
    return result



#print(sub_encrypt("KEEP THE SECRET SAFE")) # Example of substitution cipher encryption
#print(sub_decrypt("ERVYE DXVR SXFPJ")) # Example of substitution cipher decryption


from collections import Counter

def freq_analysis(text):
    letters = []
    for c in text.upper():
        if c.isalpha():
            letters.append(c)

    total = len(letters)
    freq = Counter(letters)
    for letter, count in freq.most_common():
        percentage = count / total * 100
        print(f"{letter}: {count} ({percentage:.1f}%)")
        
cipher = ("EKT YTJRTE BTYYQFT PY KPZZTO PO EKPY NQRQFRQNK. "
          "STEETR GRTCVTOJD ZXTY OXE RTHTQS EKT IKXST LTD, "
          "MVE PE FPHTY Q FXXZ YEQRE. "
          "SXXL GXR JXBBXO IXRZY, RTNTQETZ NQEETROY, "
          "QOZ YKXRE IXRZY. "
          "IKTO DXV RTJXHTR EKT BTYYQFT, "
          "EKT HPFTOTRT LTD KQY GXVR STEETRY.")


freq_analysis(cipher)

# Mapping built from frequency analysis + pattern matching
m = {'T':'E','E':'T','R':'R','Y':'S','X':'O','Q':'A','K':'H','O':'N',
     'Z':'D','P':'I','F':'G','S':'L','J':'C','B':'M','N':'P','V':'U',
     'D':'Y','H':'V','I':'W','G':'F','L':'K','C':'Q','M':'B'}
 
result = ""
for c in cipher:
    if c in m:
        result += m[c]
    else:
        result += c
print(result)

from collections import Counter

ct = ("VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZL"
      "GFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVC"
      "OPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWL"
      "GOFGGGVAQFGIEZLTUS")

# Step 1: Split ciphertext into 4 groups
group1 = ct[0::4]
group2 = ct[1::4]
group3 = ct[2::4]
group4 = ct[3::4]

# Step 2: Find most frequent letter in each group
top1 = Counter(group1).most_common(1)[0][0]
top2 = Counter(group2).most_common(1)[0][0]
top3 = Counter(group3).most_common(1)[0][0]
top4 = Counter(group4).most_common(1)[0][0]

print("Most frequent letters:", top1, top2, top3, top4)

# Step 3: Assume each top letter = E, find the shift, convert to key letter
k1 = chr((ord(top1) - ord('E')) % 26 + 65)
k2 = chr((ord(top2) - ord('E')) % 26 + 65)
k3 = chr((ord(top3) - ord('E')) % 26 + 65)
k4 = chr((ord(top4) - ord('E')) % 26 + 65)

key = k1 + k2 + k3 + k4
print("Key:", key)

# Step 4: Decrypt
result = ""
for i in range(len(ct)):
    shift = ord(key[i % 4]) - 65
    letter = chr((ord(ct[i]) - 65 - shift) % 26 + 65)
    result += letter

print("Plaintext:", result)


