def main():
    n = int(input())
    a = list(map(int, input().split()))
    rec(a, n , 0)


def rec(a, n, i):
    if(i>=n) : return
    rec(a, n, i+2)
    print(a[i], end=" ")


if __name__ == "__main__":
    main()