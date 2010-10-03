#large input in s
#  Running Time:  886.024324894
#small input in s
#  Running Time:  0.768309831619
# What changed: sorted the bases before running in the hope that
# the answers subset would be better populated. Results do seem to support 
# this: the smaller set barely changed, but the larger set went down to ~15 minutes.
#

from time import time
def run(test_case):
    start = time()
    file = open ("A-large-practice.in", "r")
    maps = int(file.readline()) + 1
    cases = []
    for i in range(1,maps):
        bases = read_int_row(file)
        bases.sort(reverse=True)
        cases.append( (i, bases) )
    cases = sorted(cases, key=lambda t: t[1])
    results = dict()
    for c in cases:
        results[c[0]] = process(c[1])

    for i in range(1, maps):
        print "Case #%d: %d" % (i, results[i])
    print "Running Time: ", time() - start

def read_int_row(file):
    return [int(x) for x in  file.readline().split(' ')]


def all_happy_for(number, bases):
    for b in bases:
        if not is_happy(number, b):
            return False
    return True

def process(bases):
    i = get_start_from_cache(bases)
    #print "Starting with i ->", i
    while True:
        i += 1
        if all_happy_for(i, bases):
            answers[tuple(bases)] = i
            return i

def get_start_from_cache(bases):
    count = len(bases)
    if count > 1:
        for i in range(count, 1, -1):
            if answers.has_key(tuple(bases[0:i])):
                #print "HIT ",bases , "  ", tuple(bases[0:i]), " -> ",answers[tuple(bases[0:i])]
                return answers[tuple(bases[0:i])]
    return 1

def is_happy(number, base):
    previous = set()
    n = number
    while n != 1:
        n = digit_sum(n, base)
        if n in previous:
            unhappy[base].add(n)
            for p in previous:
                unhappy[base].add(p)
            return False
        elif n in happy[base]:
            return True
        elif n in unhappy[base]:
            return False
        else:
            previous.add(n)
    happy[base].add(number)
    return True

def digit_sum(number, base):
    if number not in sums[base]:
        s = 0
        n = number
        while n > 0:
            s += (n % base) ** 2
            n /= base
        sums[base][number] = s
    return sums[base][number]


MAX_BASE = 10
happy = [set() for x in range(0, MAX_BASE + 1)]
unhappy = [set() for x in range(0, MAX_BASE + 1)]
sums = [dict() for x in range(0, MAX_BASE+1)]
answers = dict()
if __name__ == "__main__":
    import sys
    test_case = None
    if len(sys.argv) > 1:
        test_case = int(sys.argv[1])
    run(test_case)
