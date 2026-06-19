import time
# Import the ratings extraction function from connect.py
from connect import get_employee_ratings

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
    def _merge(left, right):
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
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return QuickSorter.sort(left) + middle + QuickSorter.sort(right)


def main():
    print("="*50)
    print(" FETCHING & SORTING EMPLOYEE RATINGS FROM SSMS DB ")
    print("="*50)
    
    # Extract raw data from your SSMS database via connect.py
    db_ratings = get_employee_ratings()
    
    if not db_ratings:
        print("No ratings found in the database or connection failed.")
        return
        
    print(f"Original Ratings pulled from DB: {db_ratings}\n")
    
    # --- 1. Bubble Sort (5.0 down to 0.0) ---
    db_bubble = db_ratings.copy()
    start_time = time.perf_counter()
    sorted_db_bubble = BubbleSorter.sort(db_bubble)[::-1]
    db_bubble_time = (time.perf_counter() - start_time) * 1000
    print(f"DB Bubble Sort Ratings (5.0 to 0.0): {sorted_db_bubble}")
    print(f"Time Taken: {db_bubble_time:.4f} ms\n")
    
    # --- 2. Merge Sort (5.0 down to 0.0) ---
    db_merge = db_ratings.copy()
    start_time = time.perf_counter()
    sorted_db_merge = MergeSorter.sort(db_merge)[::-1]
    db_merge_time = (time.perf_counter() - start_time) * 1000
    print(f"DB Merge Sort Ratings (5.0 to 0.0):  {sorted_db_merge}")
    print(f"Time Taken: {db_merge_time:.4f} ms\n")
    
    # --- 3. Quick Sort (5.0 down to 0.0) ---
    db_quick = db_ratings.copy()
    start_time = time.perf_counter()
    sorted_db_quick = QuickSorter.sort(db_quick)[::-1]
    db_quick_time = (time.perf_counter() - start_time) * 1000
    print(f"DB Quick Sort Ratings (5.0 to 0.0):  {sorted_db_quick}")
    print(f"Time Taken: {db_quick_time:.4f} ms")


if __name__ == "__main__":
    main()