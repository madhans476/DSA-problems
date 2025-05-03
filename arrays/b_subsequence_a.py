def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i, j = 0, 0

    while True:
        if i == n or j == m : break
        if (a[i] == b[j]): j+=1
        i+=1

    if (j == m): print("YES")
    else: print("NO")

if __name__ == "__main__":
    main()