# Accepted by *acebook after accounting for disjoint graphs + minor optimizations
# Removing identifying text as Mark commented on how we may not want random people
# to be able to just look up solutions.
# 
# real  0m0.023s
# user  0m0.011s
# sys 0m0.010s

# Simple algorithm: 
#  * Get shortest paths between all nodes.
#  * Run through an minimize expected time.
#
# Has obvious places for improvements;
#  * Handle disjoint graphs by spitting out -1.00.
#  * Could make dijkstra faster using a priority queue.
#  * etcs etcs

INF = 999999999999999999999
min_exp_time = INF
SORTED_KEY = '<sorted_by_probabilities_yeah_its_hacky>'

def solve(probs, conns, source):
  global min_exp_time
  all_shortest = get_all_shortests(conns, probs)
  search(all_shortest, probs, source)
  print ("%0.2f" % min_exp_time)
  
def search(all_shortest, probs, currentnode, lastnode=None, exp_time=0.0, time=0.0, prob=1, count=1, visited=None):
  global min_exp_time
  if lastnode != None:
    time += all_shortest[lastnode][currentnode]
  if visited == None:
    visited = [currentnode]
  exp_time += time * probs[currentnode]
  prob -= probs[currentnode]
  remain_exp_time = time * prob
  
  if count < len(all_shortest):
    if min_exp_time > exp_time + remain_exp_time:
      for v,_ in all_shortest[currentnode][SORTED_KEY]:
        if v not in visited:
          search(all_shortest, probs, v, currentnode, exp_time, time, prob, count +1, cons(v, visited))
  else:
    min_exp_time = min(min_exp_time, exp_time)
    exp_time_cache = exp_time
    
def get_all_shortests(conns, probs):
  shortest_paths = {}
  for k in conns.keys():
    shortest_paths[k] = get_shortest(conns, k)
    shortest_paths[k][SORTED_KEY] = sorted(shortest_paths[k].items(), key=lambda x:x[1]*(1.0-probs[x[0]]))
  return shortest_paths

def get_shortest(conns, source):
  dist = {}
  previous = {}
  for v in conns:
    dist[v] = INF
    previous[v] = None
  dist[source] = 0
  Q = conns.keys()
  while Q:
    u = get_min_vertex(Q, dist)
    if dist[u] == INF:
      break
    Q.remove(u)
    for n, v in conns[u].items():
      alt = dist[u] + v
      if alt < dist[n]:
        dist[n] = alt
        previous[n] = u
  del dist[source]
  return dist

def get_min_vertex(Q, dist):
  # could easily be sped up by using
  # a priority queue or minheap etcs
  min_vertex = Q[0]
  min_value = dist[min_vertex]
  for i in Q:
    if dist[i] < min_value:
      min_value = dist[i]
      min_vertex =i
  return min_vertex

def get_source_and_probabilities(file):
  [count] = read_int_row(file)
  probs = {}
  source = None
  for i in range(0, count):
    [name, prob] = file.readline().split(None, 1)
    if i == 0:
      source = name
    probs[name] = float(prob)
  return (source, probs)

def get_connections(file):
  count, = read_int_row(file)
  connections = {}
  for i in range(0, count):
    a,b,cost = file.readline().split(None, 2)
    if not connections.has_key(a):
      connections[a] = {}
    if not connections.has_key(b):
      connections[b] = {}
    connections[a][b] = int(cost)
    connections[b][a] = int(cost)
  return connections

def cons(x, xs):
    return [x] + xs
def read_int_row(file, delimiter=' '):
  return [int(x) for x in file.readline().split(delimiter) if x != '']

if __name__ == '__main__':
  import sys
  file = open(sys.argv[1],"r")
  source, probs = get_source_and_probabilities(file)
  conns = get_connections(file)
  solve(probs, conns, source)
