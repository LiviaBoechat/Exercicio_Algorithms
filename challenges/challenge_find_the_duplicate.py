def find_duplicate(nums):
    if not nums or len(nums) == 1:
        return False

    if any(type(num) == str or num < 0 for num in nums):
        return False

    counter = set()
    for num in nums:
        if num in counter:
            return num
        counter.add(num)

    return False


print(find_duplicate([1, 'b', 3, 4, 'a']))    # False
print(find_duplicate([1, 2, 3, 4, 4]))        # 4
print(find_duplicate([1]))                    # False
print(find_duplicate([]))                     # False
print(find_duplicate(["string"]))             # False
