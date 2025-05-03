def main():
    n = int(input())

    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    pd = 0
    for i in range(n):
        pd += (matrix[i][i])
    
    sd = 0
    for j in range(n):
        sd += (matrix[j][n-j-1])

    print(abs(pd-sd))

    

if __name__ == "__main__":
    main()