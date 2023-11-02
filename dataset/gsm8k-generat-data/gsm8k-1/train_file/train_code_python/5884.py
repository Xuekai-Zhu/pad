def solution():
    """Dan is learning to screen-print t-shirts to sell at the craft fair. He makes t-shirts, over the first hour, at the rate of one every 12 minutes. Then, in the second hour, he makes one at the rate of every 6 minutes. How many t-shirts does he make over the course of those two hours?"""
    tshirts_first_hour = 60 // 12
    tshirts_second_hour = 60 // 6
    total_tshirts = tshirts_first_hour + tshirts_second_hour
    result = total_tshirts
    return result

print(solution())