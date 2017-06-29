import random

def twoSum(nums, target):
    if type(nums) != list:
        raise TypeError("nums must be a list")
    if len(nums) <= 1:
        raise ValueError("length of nums should be larger than 1")
    ret = []
    max_index = len(nums)
    for i in range(0, max_index):
        tmp = target - nums[i]
        if (tmp in nums) & (tmp != nums[i]):
            ret.append(i)
            ret.append(nums.index(tmp))
            return ret
    return None

if __name__ == "__main__":
    nums = []
    for i in range(0, 10):
        nums.append(random.randint(0,100))
    target = random.randint(1, 200)
    ret = twoSum(nums, target)
    print "nums are:{0}, target is:{1}".format(nums, target)
    if ret:
        print "two sum result is:{0}".format(ret)
    else:
        print "No result matching."