def merge_and_count(arr, left, mid, right):
    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]

    i = 0
    j = 0
    k = left
    inv_count = 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
            inv_count += (len(left_part) - i)  # Remaining left side are all inversions
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

    return inv_count

def merge_sort_and_count(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_and_count(arr, left, mid)
        inv_count += merge_sort_and_count(arr, mid+1, right)
        inv_count += merge_and_count(arr, left, mid, right)
    return inv_count

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
print("Number of inversions:", merge_sort_and_count(arr, 0, n-1))
