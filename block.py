import sha3

s = "block_header"
nonce = 0

while True:
  hash = sha3.sha3_256((s + str(nonce)).encode("utf8")).hexdigest()
  if hash[0:6] == "000000": break
  nonce = nonce + 1

print(s + str(nonce))
print(hash)
