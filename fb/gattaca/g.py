#!/usr/bin/python
# Solution to the facebook gattaca problem.
#  solved in nlogn. I have a feeling it could be done in n
#  but I need to go do some real work :)
#  passed fb hen submitted with a few changes.
#   What changes? Thats left as an exercise to the reader :)

class Prediction:
  def __init__(self, triple):
    assert(len(triple) == 3)
    self.start = triple[0]
    self.stop = triple[1]
    self.score = triple[2]
  def __repr__(self):
    return ", ".join(str(x) for x in [self.start, self.stop, self.score])

def solve(predictions):
  sorted_by_stop = sorted(predictions, key=lambda p:p.stop)
  prevs = get_prevs(sorted_by_stop)
  scores = [0, 0] 
  for i, current in enumerate(sorted_by_stop):
    current_cum_score = current.score + scores[prevs[i]+1]
    scores.append(max(scores[-1], current_cum_score))
  return scores[-1]

def get_prevs(sorted_by_stop):
  from bisect import bisect
  prevs = {}
  stops = [x.stop for x in sorted_by_stop]
  for i, p in enumerate(sorted_by_stop):
    prevs[i] = bisect(stops, p.start)
  return prevs
  
def get_predictions(file):
  count = read_int_row(file)[0]
  for i in range(0, (count + 79)/80):
    file.readline()
  prediction_count = read_int_row(file)[0]
  for i in range(0, prediction_count):
    yield Prediction(read_int_row(file))

def read_int_row(file, delimiter=' '):
  return [int(x) for x in file.readline().split(delimiter) if x != '']

if __name__ == "__main__":
  import sys
  assert(len(sys.argv) == 2)
  print solve(get_predictions(open(sys.argv[1], "r")))
