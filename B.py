num_of_lines = input()
lines = []

for i in range(num_of_lines):
    line = raw_input()
    lines.append(line)


def process(line):
    count = 0
    A, B = [int(x) for x in line.split()]

    for n in xrange(A, B):
        s = str(n)
        possibles = [j for j, i in enumerate(s[1:]) if int(i) <= int(str(B)[0])]

        for possible in possibles:
            possible += 1
            p = s[possible:] + s[:possible]

            m = int(p)

            if A <= n < m <= B:
                count += 1
    return count

for line_num, line in enumerate(lines, 1):

    x = process(line)

    print "Case #%s: %s" % (line_num, x)
