#! /usr/bin/python

number = 0

f = open('index.html', 'w')
textIn = open('lines.txt', 'r')

for line in textIn:
    f.write('<input type="checkbox" name="%s" value="true" /> <label for="%s">%s</label><br />\n' % (number, line, line))
    number += 1


textIn.close()
f.close()
