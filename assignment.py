while True:
  try:
    x=int(input())
    y=0
    if x < 1:
      print("Enter a number more than 0")
    else:
      for i in range(x):
        if i % 2==0:
          y= y + 1 / (2 * i + 1)
        else:
          y=y-1 / (2 * i + 1)
      y=y*4

      print(round(y,3))
  except ValueError:
    print("Enter a valid number")
