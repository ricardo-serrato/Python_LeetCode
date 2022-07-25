
def containsDuplicate(nums):

    s = set(nums)

    return len(nums) > len(s)


# solution: 2
    # d = {}

    # for number in nums:
    #     if number not in d:
    #         d[number] = 1
    #     else:
    #         return True

    # return False

