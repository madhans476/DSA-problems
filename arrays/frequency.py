def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))

    hashmap = {}
    for val in a:
        hashmap[val] = hashmap.get(val, 0)+1
    
    for i in range(1,m+1):
        print(hashmap.get(i, 0))

if __name__ == "__main__":
    main()