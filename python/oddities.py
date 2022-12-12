n = int(input())

for i in range(n):
    x = int(input())
    print(f"{x} is even" if x % 2 == 0 else f"{x} is odd")
