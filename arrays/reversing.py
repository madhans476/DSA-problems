def main():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        if a[i] == 0:
            st, end = 0, i-1
            while st < end:
                temp = a[st] 
                a[st] = a[end]
                a[end] = temp
                st+=1
                end-=1
    
    for val in a:
        print(val , end=" ")
            

if __name__ == "__main__":
    main()