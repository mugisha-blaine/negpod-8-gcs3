nums_dict = {}
def sum(integes, target):
    for i, num in enumerate(nums):
        if target - num in nums_dict:
            return (nums_dict[target-num], i)
        nums_dict[num] = i

nums =[2,7,11,15]
targ = 9
print(sum(nums, targ))

