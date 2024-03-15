filePath = 'input/day6.txt'

with open(filePath) as f:
    lines = f.readlines()
    time = []
    distance = []
    for line in lines:
        line = line.strip()
        parts = line.split(': ')
        if parts[0] == 'Time':
            time.extend([int(value) for value in parts[1].split()])
        elif parts[0] == 'Distance':
            distance.extend([int(value) for value in parts[1].split()])

countlist = []  

for i in range(len(time)):
    count = 0
    for j in range(time[i] + 1):
        chargetime = j
        runtime = time[i] - chargetime
        distanceRan =   chargetime * runtime
        if distanceRan > distance[i]:  
            count += 1
    countlist.append(count)

product = 1
for count in countlist:
    product *= count

print(product)

with open(filePath) as f:
  lines = f.readlines()
  time, distance = [], []
  for line in lines:
      line = line.strip()
      parts = line.split(': ')
      if parts[0] == 'Time':
          time.extend([int(''.join(parts[1].split()))])
      elif parts[0] == 'Distance':
          distance.extend([int(''.join(parts[1].split()))])


countlist = []  

for i in range(len(time)):
    count = 0
    for j in range(time[i] + 1):
        chargetime = j
        runtime = time[i] - chargetime
        distanceRan =   chargetime * runtime
        if distanceRan > distance[i]:  
            count += 1
    countlist.append(count)

product = 1
for count in countlist:
    product *= count

print(product)