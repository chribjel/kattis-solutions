num = int(input())

if num < 99:
  print(99)
elif num % 100 < 49:
  print(num - (num % 100)-1)
else:
  print(num + (100 - num % 100)-1)
