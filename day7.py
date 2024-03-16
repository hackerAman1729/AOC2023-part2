filePath = 'input/day7.txt'

def divideByType(Hand):
    dict = {}
    for i in Hand: 
      if i in dict:
          dict[i] += 1
      else:
          dict[i] = 1

    return dict



with open(filePath) as f:
    lines = f.readlines()
    hand = []
    bid = []
    for line in lines:
      line = line.strip()
      parts = line.split(' ')
      hand.append(parts[0])
      bid.append(int(parts[1]))

highcard = []
onepair = []
twopair= []
threepair = []
fullhouse = []
fourpair = []
fivepair = []

for i in hand:
  returnDict  = (divideByType(i))
  length = len(returnDict)
  if 5 in returnDict.values() :
    fivepair.extend(i)
  elif 4 in returnDict.values() and 1 in returnDict.values():
      fourpair.extend(i)
  elif 3 in returnDict.values() and 2 in returnDict.values():
      fullhouse.extend(i)
  elif 3 in returnDict.values() and 1 in returnDict.values():
      threepair.extend(i)
  elif 2 in returnDict.values() and length == 3:
      twopair.extend(i)
  elif 2 in returnDict.values() and length == 4:
      onepair.extend(i)
  elif 1 in returnDict.values() and length == 5:
      highcard.extend(i)
      
ranks = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
for i in highcard:
  
  

  