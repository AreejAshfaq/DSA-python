#Question:
#You are given a sorted array of integers arr and a target integer x.
#Write an algorithm to find the index of x in
#the array using binary search. If x is not found, return -1.
#Input:
"""	A sorted array arr of integers.
	•	An integer x (the target value).

Output:

	•	Return the index of x in the array, or -1 if x is not found.

Example:

Input: arr = [2, 5, 7, 10, 14, 20], x = 10
Output: 3

Input: arr = [1, 4, 6, 8, 9], x = 3
Output: -1

Constraints:

	•	Time complexity should be O(log n).
	•	The array is sorted in ascending order"""

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1


### Example Usage


# Example 1
arr1 = [2, 5, 7, 10, 14, 20]
x1 = 10
print(binary_search(arr1, x1))  # Output: 3

# Example 2
arr2 = [1, 4, 6, 8, 9]
x2 = 3
print(binary_search(arr2, x2))  # Output: -1
""" This program is based on the binary search algorithm, which is used to find a specific element in a sorted array. Let's break it down step by step:

1. Function Definition: 
   - def binary_search(arr, x): This function takes two parameters, arr (the array where we want to search) and x (the value we want to find).

2. Initializing Pointers:
   - left, right = 0, len(arr) - 1: This sets the left pointer at the start of the array and the right pointer at the end of the array.

3. While Loop:
   - while left <= right: This loop continues as long as the left pointer is less than or equal to the right pointer.

4. Finding Midpoint:
   - mid = left + (right - left) // 2: This calculates the midpoint where we check if x is located.

5. Comparison:
   - if arr[mid] == x: If the value at the midpoint is equal to x, we return the index of mid.
   - elif arr[mid] < x: If the value at the midpoint is less than x, it means x must be in the right half, so we set the left pointer to mid + 1.
   - else: If the value at the midpoint is greater than x, it means x must be in the left half, so we set the right pointer to mid - 1.

6. Not Found Case:
   - If the loop ends and x is not found, the function returns -1.

This way, the program efficiently finds an element in a sorted array. If you need any further clarification or examples, just let me know!"""