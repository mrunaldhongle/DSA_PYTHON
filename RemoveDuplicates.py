#Remove Duplicates from Sorted Array
def remove_duplicates(nums):
    if not nums:
        return 0
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j+=1
            nums[j] = nums[i]
    return j + 1
nums = list(map(int, input("Enter a sorted array of numbers separated by spaces: ").split()))
n = remove_duplicates(nums)
print(' '.join(map(str, nums[:n])))
