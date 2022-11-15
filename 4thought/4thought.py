m = int(input())

ops = ['+', '-', '*', '//']

for i in range(m):
  n = int(input().replace("/", "//"))

  for op in ops:
    for op2 in ops:
      for op3 in ops:
          if eval("4" + op + "4" + op2 + "4" + op3 + "4") == n:
            print(("4 " + op + " 4 " + op2 + " 4 " + op3 + " 4 " + " = " + str(n)).replace("//", "/"))
            break
      else:
        continue
      break
    else:
      continue
    break
  else:
    print("no solution")
