def find_duplicate(nums):
    """ Faça o código aqui. """
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                if nums[x] < 0:
                    return False
                return nums[x]
    return False


nums = [3, 1, 3, 4, 2]
print(find_duplicate(nums))
