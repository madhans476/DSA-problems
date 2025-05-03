def main():
    n = int(input())
    rec(n)

def rec(n):
    print(n, end=" ")
    if n == 1: return
    if n%2 == 0 : rec(int(n/2))
    else: rec((n*3)+1)

if __name__ == "__main__":
    main()