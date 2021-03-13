def selection_sort(arr):

    count = 0
    
    for j in range(len(arr)-1):
        
        min = j
        
        for i in range(j, len(arr)):
            if arr[min] > arr[i]:
                min = i
            
        arr[j], arr[min] = arr[min], arr[j]
        count += 1

        print("Iteration", count, "-",arr)

selection_sort([10,8,6,4,2,0,9,7,5,3,1])