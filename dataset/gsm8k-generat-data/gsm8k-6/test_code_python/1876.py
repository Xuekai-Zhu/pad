def solution():
    # Calculate the total number of gift bags Carl needs to make
    total_gift_bags = 10 + 20 + 50 + 40  # 10 extravagant gift bags, 20 average gift bags, 50 expected guests, and 40 additional guests

    # Calculate the number of bags Carl needs to make beyond the 30 he's already made
    bags_to_make = total_gift_bags - 30  # Carl has already made 30 gift bags

    result = bags_to_make
    return result

print(solution())