def is_safe(nums):
    last = -1
    direction = "none"
    for index, num in enumerate(nums):
        num = int(num)
        if last == -1:
            last = num
            continue
        else:
            if abs(num - last) > 3 or abs(num - last) < 1:
                return False, index
            if num > last:
                if direction == "decreasing":
                    return False, index
                direction = "increasing"
            if num < last:
                if direction == "increasing":
                    return False, index
                direction = "decreasing"
            last = num
    return True, -1


def count_safe_lines(ls):
    total_safe = 0
    for item in ls:
        nums = item.split()
        if is_safe(nums)[0]:
            total_safe += 1
    return total_safe


def count_safe_lines_tolerator(ls):
    total_safe = 0
    for item in ls:
        nums = item.split()
        safe, index = is_safe(nums)
        if safe:
            total_safe += 1
        else:
            temp = nums[:]
            temp.pop(index)
            nums_1 = temp
            temp = nums[:]
            temp.pop(index-1)
            nums_2 = temp
            if is_safe(nums_1)[0] or is_safe(nums_2)[0]:
                total_safe += 1
            elif index == 2:
                temp = nums[:]
                temp.pop(0)
                if is_safe(temp)[0]:
                    total_safe += 1
    return total_safe


def brute_force(ls):
    total_safe = 0
    for item in ls:
        nums = item.split()
        for index in range(len(nums)):
            temp = nums[:]
            temp.pop(index)
            if is_safe(temp)[0]:
                total_safe += 1
                break
    return total_safe
