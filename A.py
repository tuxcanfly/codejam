from string import maketrans

x = {' ': ' ', 'a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 'i', 'g': 'l', 'f': 'w', 'i': 'k', 'h': 'b', 'k': 'o', 'j': 'u', 'm': 'x', 'l': 'm', 'o': 'e', 'n': 's', 'q': 'z', 'p': 'v', 's': 'd', 'r': 'p', 'u': 'j', 't': 'r', 'w': 't', 'v': 'g', 'y': 'a', 'x': 'h', 'z': 'q'}

translation_table = maketrans(''.join(x.values()), ''.join(x.keys()), )


num_of_lines = input()
lines = []

for i in range(num_of_lines):
    line = raw_input()
    lines.append(line)


for line_num, line in enumerate(lines, 1):
    print "Case #%s: %s" % (line_num, line.translate(translation_table))
