def main():
    n = int(input())
    a = list(map(int, input().split()))

    res = sum(a)
    print(abs(res))


if __name__ == "__main__":
    main()