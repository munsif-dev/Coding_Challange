if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    def findMax(n,arr):
        max = arr[0]
        for i in range(n):
            if arr[i] > max:
                max = arr[i]
        return max
    
    championScore= findMax(n,arr)
    arr2 = [arr[i] for i in range(n) if arr[i] != championScore]
    n2 = len(arr2)
    runnerUp = findMax(n2,arr2)
    
    print(runnerUp)
    
    
    
