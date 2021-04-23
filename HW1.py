import re
seq=''
name=''
with open('isocitrate lyase.fasta', "r") as inpf:
  for line in inpf:
    if ">" not in line:
      seq+=line.strip()
    else:
      name+=line.strip()

namef=re.search(r"\b\w.*\d", name)
res=re.search(r"K[KR]CGH[LMQR]", seq)
print(f'Isocitrate lyase ({namef.group()}) contains its active site {res.group()} starting from {res.start()} position')
