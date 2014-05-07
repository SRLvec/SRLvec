import SRL

"""
inputFile = '/Users/charleywu/Desktop/senna/examples/Books/The Two Sources of Morality And Religion.txt'
test = SRL.senna(inputFile, 'sources')
test.call()
test.roleLabel()
test.drawTree(test.post_ids[5])

"""



input = "You wouldn't believe how I respect you, Alyosha, for never telling lies"
test = SRL.senna(input)
test.callFromString()
check = test.roleLabel()
print check
test.drawTree(test.post_ids[0])