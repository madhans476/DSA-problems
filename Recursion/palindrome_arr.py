def main():
    n = int(input())
    a = list(map(int, input().split()))
    res = rec(a, 0, n-1)
    print("YES" if res == 1 else "NO")

def rec(a, l , r):
    if(l>=r) : return 1
    res = rec(a, l+1, r-1)
    return res and (a[l]==a[r])

if __name__ == "__main__":
    main()