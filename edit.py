#! /usr/bin/python

number = 0

f = open('lines.html', 'w')
textIn = open('lines.txt', 'r')

for line in textIn:
    f.write('<input type="checkbox" name="%s" id="%s" value="true" /> <label for="%s">%s</label><br />\n' % (number, number, number, line))
    number += 1


textIn.close()
f.close()
