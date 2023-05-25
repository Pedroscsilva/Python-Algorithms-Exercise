def find_duplicate(nums):
    if not isinstance(nums, list):
        return False

    nums = sorted(nums)

    for i in range(0, len(nums) - 1):
        if not isinstance(nums[i], int) or nums[i] <= 0:
            return False
        if nums[i] == nums[i - 1]:
            return nums[i]

    return False
