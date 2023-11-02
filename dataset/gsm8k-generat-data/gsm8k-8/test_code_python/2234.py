def solution():
    # Calculate how much Susie earned last week
    total_earning = 3 * 7 * 10

    # Calculate how much Susie spent on make-up
    makeup_cost = total_earning * 3/10

    # Calculate how much Susie spent on skincare products
    skincare_cost = total_earning * 2/5

    # Calculate how much Susie has left
    remaining_money = total_earning - makeup_cost - skincare_cost
    result = remaining_money
    return result

print(solution())