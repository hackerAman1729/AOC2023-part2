#part 1. part2 :(

def loadData(filePath):
  with open(filePath) as f:
      data = f.read().strip().split('\n\n')
  instructions = data[0]
  nodeMap = {}
  for line in data[1].split('\n'):
      node, connections = line.split(' = ')
      nodeMap[node] = tuple(connections[1:-1].split(', '))
  return instructions, nodeMap

def navigate(instructions, nodeMap):
  currentNode = 'AAA'
  step = 0
  instructionIndex = 0
  while currentNode != 'ZZZ':
      direction = instructions[instructionIndex % len(instructions)]
      currentNode = nodeMap[currentNode][0 if direction == 'L' else 1]
      instructionIndex += 1
      step += 1
  return step



instructions, nodeMap = loadData('input/day8.txt')
print(navigate(instructions, nodeMap))

