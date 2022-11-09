k, m, n = map(int, input().split())

if k % (m+n) >= m:
  print("Alex")
else:
  print("Barb")
