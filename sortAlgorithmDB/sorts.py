import time

def userInput():
    while True:
        user_input = input("Enter a long number to be sorted (e.g., 123456789): ").strip()
        
        if user_input.isdigit():
            break  
        else:
            print("Invalid input. Please enter numbers only (no letters, spaces, or symbols).")
    return user_input


class BubbleSorter:
    @staticmethod
    def sort(arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

class MergeSorter:
    @staticmethod
    def sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        leftHalf = MergeSorter.sort(arr[:mid])
        rightHalf = MergeSorter.sort(arr[mid:])
        return MergeSorter._merge(leftHalf, rightHalf)
    @staticmethod
    def _merge(left,right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        return result

class QuickSorter:
    @staticmethod
    def sort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return QuickSorter.sort(left) + middle + QuickSorter.sort(right)
    
    
def main():
    rawString = userInput()
    master_list = [int(digit) for digit in rawString]
    print(f"\nOriginal Input: {master_list}")
    
    bubble_data = master_list.copy() 
    start_time = time.perf_counter() # Start Timer
    sorted_bubble = BubbleSorter.sort(bubble_data)
    end_time = time.perf_counter()   # End Timer
    bubble_elapsed = (end_time - start_time) * 1000 
    
    print(f"\nBubble Sort: {sorted_bubble}")
    print(f"Time Taken:  {bubble_elapsed:.4f} ms")
    
    merge_data = master_list.copy()
    start_time = time.perf_counter()
    sorted_merge = MergeSorter.sort(merge_data)
    end_time = time.perf_counter()
    merge_elapsed = (end_time - start_time) * 1000
    
    print(f"\nMerge Sort:  {sorted_merge}")
    print(f"Time Taken:  {merge_elapsed:.4f} ms")
    

    quick_data = master_list.copy()
    start_time = time.perf_counter()

    sorted_quick = QuickSorter.sort(quick_data)
    end_time = time.perf_counter()
    quick_elapsed = (end_time - start_time) * 1000
    
    print(f"\nQuick Sort:  {sorted_quick}")
    print(f"Time Taken:  {quick_elapsed:.4f} ms")


if __name__ == "__main__":
    main()