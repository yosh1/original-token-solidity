import sha3

MAX_NONCE = 2**64

def calc_hash(block_header, nonce):
  s = (str(block_header) + str(nonce)).encode("utf8")
  return sha3.sha3_256(s).hexdigest()

def get_target(difficulty):
  return 2**256 // difficulty

def mine(block_header, difficulty):
  target = get_target(difficulty)
  nonce = 0
  while nonce < MAX_NONCE:
    result = calc_hash(block_header, nonce)
    if int(result, 16) < target: break
    nonce += 1
  return nonce

def verify(block_header, nonce, difficulty):
  h = calc_hash(block_header, nonce)
  if int(h, 16) < get_target(difficulty):
    return (True, h)
  else:
    return (False, "")

dummy_data = "dummy data"
prev_hash = "0" * 64

for i in range(1, 32):
  difficulty = 2 ** i
  print("mining... [difficulty: %d]" % difficulty)
  block_header = dummy_data + prev_hash
  nonce = mine(block_header, difficulty)

  result, block_hash \
  = verify(block_header, nonce, difficulty)
  if not result:
    print("Failed!")
    break
 
  print("Target: 0x%064x" % get_target(difficulty))
  print("Hash  : 0x%s" % block_hash)
  print("Nonce : %d" % nonce)
  print("-"*74)
  prev_hash = block_hash
