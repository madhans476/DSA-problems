def main():
    n, k = map(int, input().split())
    max_and , max_or, max_xor = 0,0,0

    for i in range(1,n+1):
        for j in range(i+1, n+1):
            if i&j > max_and and i&j <k:
                max_and = i&j
            if i|j > max_or and i|j < k:
                max_or = i|j
            if i^j > max_xor and i^j <k:
                max_xor = i^j

    print(max_and)
    print(max_or)
    print(max_xor)


if __name__=="__main__":
    main()