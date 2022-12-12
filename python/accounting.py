n_q = input().split()
n, q = int(n_q[0]), int(n_q[1])

global_amount = 0

accounts = {}

for i in range(q):
  query = input().split()
  if query[0] == "SET":
    accounts[int(query[1])] = int(query[2])
  elif query[0] == "RESTART":
    accounts = {}
    global_amount = int(query[1])
  elif query[0] == "PRINT":
    if int(query[1]) in accounts:
      print(accounts[int(query[1])])
    else:
      print(global_amount)
