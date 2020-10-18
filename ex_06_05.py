#Working with strings
text = "X-DSPAM-Confidence:    0.8475"
atpos = text.find('0')
print(atpos)
sspos= text.find('5',atpos)
print(sspos)
number= text[atpos:sspos+1]
print(float(number))
