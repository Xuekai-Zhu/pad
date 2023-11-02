def solution():
    length = 8
    width = 4
    height = 1
    cubic_feet_per_bag = 4
    total_cubic_feet = length * width * height
    total_bags = total_cubic_feet / cubic_feet_per_bag
    result = total_bags
    return result

print(solution())