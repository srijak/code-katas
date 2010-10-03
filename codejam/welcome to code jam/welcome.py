# Tested and verified with both large and small input.
# time python wtcj.py
# real  0m1.005s
# user  0m0.580s
# sys 0m0.020s

TARGET = "welcome to code jam".lower()

def run(test_case):
    file = open ("example.in", "r")
    lines = int(file.readline()) + 1
    for i in range(1,lines):
        print "Case #%d:" % i,
        line = file.readline().lower()
        if test_case == None:
            process(line)
        elif test_case == i:
            process(line)
def log(str):
    print str

def process(line):
    start = line.find('w')
    end  = len(line) - line[::-1].find('m')
    import re
    line = re.sub("[^welcomtdja ]","", line[start:end])
    count = generate(TARGET, line)
    print "%04d" % count

def generate(target, line):
    candidates = []
    for j, looking_for in enumerate(target):
        candidates.append([])
        for i, char in enumerate(line):
            # find all candidates
            #  which are all places that have the char in the line
            # for each of these, workout how many are prefixed correctly
            if char == looking_for:
                prev_match = 1
                if j > 0:
                    prev_match = sum([x[1] for x in candidates[j-1] if x[0] < i])
                candidates[j].append((i, prev_match))
    last = candidates[len(target)-1]
    if len(last) > 0:
        return sum([x[1] for x in last])
    else:
        return 0

if __name__ == "__main__":
    import sys
    test_case = None
    if len(sys.argv) > 1:
        test_case = int(sys.argv[1])
    run(test_case)


