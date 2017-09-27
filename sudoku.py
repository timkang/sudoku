dog = [
    [945,945,945,945,945,945,945,945,945],
    [945,945,945,945,945,945,945,945,945],
    [945,945,945,945,945,945,945,945,945],
    [945,945,945,945,945,945,945,945,945],
    [945,945,945,945,945,945,945,945,945],
    [945,945,945,945,945,945,945,945,945],
    [945,945,945,945,945,945,945,945,945],
    [945,945,945,945,945,945,945,945,945],
    [945,945,945,945,945,945,945,945,945]
  ]

cat = []

#0-3 3-6 6-9
def goat(x, y, num):

  if x < 3:
    minX = 0
    maxX = 3
  elif x < 6:
    minX = 3
    maxX = 6
  elif x < 9:
    minX = 6
    maxX = 9

  if y < 3:
    minY = 0
    maxY = 3
  elif y < 6:
    minY = 3
    maxY = 6
  elif y < 9:
    minY = 6
    maxY = 9    

  for count1 in range(minX, maxX):
    for count2 in range(minY, maxY):
      dog[count1][count2] = dog[count1][count2] - 100 - num
      
  for count1 in range(0,9):
    for count2 in range(0,9):
      if count1 == x and (count2 < minY or count2 >= maxY):
        dog[count1][count2] = dog[count1][count2] - 100 - num
      if count2 == y and (count1 < minX or count1 >= maxX):
        dog[count1][count2] = dog[count1][count2] - 100 - num
  
  dog[x][y] = 100 + num;
  for line in dog:
    print(line)

while True:
  person = input("Please input x, y, num : ").split(",")
  goat(int(person[0]), int(person[1]), int(person[2]))
  
