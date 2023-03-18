def order(numbers, target):
    if target not in numbers:
        numbers.append(target)    

    x = sorted(numbers)
    return x.index(target)
nums = [1,3,5,6]
target = 7

print(order(nums, target))
