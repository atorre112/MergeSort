def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle of the array
        left_half = arr[:mid]  # Dividing the elements into 2 halves
        right_half = arr[mid:]

        # Recursively sorting both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merging the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)
