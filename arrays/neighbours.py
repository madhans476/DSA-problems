def main():
    n, m = map(int , input().split())
    mat = []
    for _ in range(n):
        row = list(input().strip())
        mat.append(row)
    
    i, j = map(int, input().split())
    check1, check2, check3, check4 = False, False, False, False


    if (j==1 or mat[i-1][j-2] == 'x'): check1 = True
    if (j==m or mat[i-1][j] == 'x'): check2 = True
    if (i==1 or mat[i-2][j-1] == 'x'): check3 = True
    if (i==n or mat[i][j-1] == 'x'): check4 = True

    print("yes" if (check1 and check2 and check3 and check4) else "no")

if __name__ == "__main__":
    main()