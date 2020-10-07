# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    A = B = 0
    C = []
    while True:
        if A == len(arrA):
            C.extend(arrB[B:])
            break
        elif B == len(arrB):
            C.extend(arrA[A:])
            break
        elif arrA[A] <= arrB[B]:
            C.append(arrA[A])
            A += 1
        else: 
            C.append(arrB[B])
            B += 1
    return C
    # while A < len(arrA) and B < len(arrB):
    #     if arrA[A] < arrB[B]:
    #         arr3[C] = arrA[A]
    #         C = C + 1
    #         A = A + 1
    #     else:
    #         arr3[C] = arrB[B]
    #         C = C + 1
    #         B = B + 1
    # while A < len(arrA):
    #     arr3[C] = arrA[A]
    #     C = C + 1
    #     A = A + 1
    # while B < len(arrB):
    #     arr3[C] = arrB[B]
    #     C = C + 1
    #     B = B + 1
    # return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    def sort(a, low, high):
        if low >= high:
            return
        p = low
        for i in range(low,high):
            if a[i] < a[p]:
                a[p+1], a[i] = a[i], a[p+1]
                a[p+1], a[p] = a[p], a[p+1]
        sort(a, low, p)
        sort(a, p + 1, high)
    sort(arr, 0, len(arr))

    return arr
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

