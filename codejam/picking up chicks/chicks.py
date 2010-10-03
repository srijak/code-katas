#!/usr/bin/python
# 
#Not the best code I've written. Various places where code can be cleaned up/ optimized.
#But, since the large input is processed at approx 0.08s, I'm not going to bother.
#$ time python chicks.py B-large-practice.in > big.in
# real    0m0.076s
# user    0m0.060s
# sys     0m0.013s

class Testcase:
  def __init__(self,case, b, t, x, v, k, n):
    self.case = case
    self.b = b
    self.t = t
    self.x = x
    self.v = v
    self.k = k
    self.n = n
  def __repr__(self):
    return "B: "+ str(self.b) + " T:"+ str(self.t) + " K:" + str(self.k) + " N:" +str(self.n) + " X:" + str(self.x) + " V:" + str(self.v)

def done(result, tc):
  print "Case #%d: %s" % (tc.case, result)

def solve(tc):
  #print tc
  have_req_speed =[]
  for i in range(0, tc.n):
    loc = tc.x[i]
    vel = tc.v[i]
    if (tc.b - loc) > (vel * tc.t):
      #barn is too far away
      have_req_speed.append(False)
    else:
      #can reach barn if no chick slower is ahead
      have_req_speed.append(True)
  possibles = len([x for x in have_req_speed if x == True]) 
  if possibles < tc.k:
    done("IMPOSSIBLE", tc)
  elif possibles == tc.n:
    done(0, tc)
  else:
    current_k = 0
    swaps = 0
    for i in range(tc.n-1, -1,-1):
      if have_req_speed[i]:
        # possible
        swaps += get_swaps_required(i, have_req_speed)
        current_k += 1
        if current_k == tc.k:
          break
    done(swaps,tc)

def get_swaps_required(chick, have_req_speed):
  # get swaps required before this can 
  # be in front of all chickens that will never make it
  return len([x for x in have_req_speed[chick:] if x == False])

def get_testcases(file):
  count, = read_int_row(file)
  for i in range(0, count):
    n,k,b,t = read_int_row(file)
    xs = read_int_row(file)
    vs = read_int_row(file)
    yield Testcase(i+1, b, t, xs, vs, k, n)

def read_int_row(file, delimiter=' '):
  return [int(x) for x in file.readline().split(delimiter) if x != '']

if __name__ == "__main__":
  import sys
  fileName = "example.in"
  if len(sys.argv) > 1:
    fileName = sys.argv[1]
  for testcase in get_testcases(open(fileName, 'r')):
    solve(testcase)
