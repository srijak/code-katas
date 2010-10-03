MAX_D = 6
primes = []

def gen_primes(limit):
  #stolen from somewhere.
  if limit <= 2:
    return []
  sieve = range(3, limit, 2)
  top = len(sieve)
  for si in sieve:
    if si:
      bottom = (si*si - 3) // 2
      if bottom >= top:
        break
      sieve[bottom::si] = [0] * -((bottom - top) // si)
  return [2] + [el for el in sieve if el]

class Testcase:
  def __init__(self, D, Seq):
    self.d = D
    self.seq = Seq

def is_valid(seq, a, b, p):
  prev = None
  for cur in seq:
    if not prev:
      prev = cur
      continue
    exp = ((a * prev + b) % p)
    if (cur != exp):
      return False
    prev = cur
  return True

def get_next(tc):
  pp = [x for x in primes if x > max(tc.seq) and x < (10 ** tc.d)]
  found = {}
  for p in pp:
    s2s1 = account_for_mod(tc.seq[2], tc.seq[1], p)
    s1s0 = account_for_mod(tc.seq[1], tc.seq[0], p)
    a = get_a(p, s2s1, s1s0)
    if not a:
      continue
    b = get_b(a, tc.seq[2], tc.seq[1], p)
    if is_valid(tc.seq, a, b, p):
      pnext = ((a*tc.seq[-1]) + b) % p
      found[pnext] = True
      if (len(found.keys()) > 1):
        break
  if len(found.keys()) != 1:
    if (len(found.keys()) == 0):
      #print tc.seq, "    " , found.keys()
      #check and see if this is a special case
      if (max(tc.seq[1:]) == min(tc.seq[1:])):
        return tc.seq[1]
    return "I don't know."
  else:
    return found.keys()[0]

def get_a(p, s2s1, s1s0):
  # s2-s1 =  a(s1-s0) % p  ... 1
  #  a = (s2 -s1)/(s1-s0)  ... 2
  #brute force value of a, such that 1 is valid
  for i in range(1, p):
    if (s2s1 == (i * s1s0) % p):
      return i
  return None

def account_for_mod(sn1, sn0, p):
  t = sn1 - sn0
  if t < 0 :
    return t + p
  else:
    return t

def get_b(a, s2, s1, p):
  # b= s2 - (as1 % p)      ... 3
  t = s2 - ((a * s1) % p)
  if t < 0:
    return t + p
  return t

def solve(tc):
  if (len(tc.seq) == 2):
    if tc.seq[0] == tc.seq[1]:
      return tc.seq[0]
    else:
      return "I don't know."
  
  if (len(tc.seq) > 1):
    return get_next(tc)
  else:
    return "I don't know."

def get_testcase(file):
  D, K = read_int_row(file) 
  seq = read_int_row(file)
  return Testcase(D, seq)

def read_int_row(file, delimiter=' '):
  return [int(x) for x in file.readline().split(delimiter) if x != '']

if __name__ == "__main__":
  f = "example.in"
  import sys
  if (len(sys.argv) >1):
    f = sys.argv[1]
  primes = gen_primes(10 ** MAX_D)
  file = open(f, "r")
  testcases = int(file.readline())
  for i in range(1, testcases + 1):
    print "Case #%d: %s" % (i, solve(get_testcase(file)))
