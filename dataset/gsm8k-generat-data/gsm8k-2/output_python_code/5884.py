def solution():
    """As Dan is learning to screen-print t-shirts to sell at the craft fair, he makes t-shirts, over the first hour, at the rate of one every 12 minutes. Then, in the second hour, he makes one at the rate of every 6 minutes. How many t-shirts does he make over the course of those two hours?"""
    first_hour_rate = 12
    second_hour_rate = 6
    first_hour_tshirts = 60 / first_hour_rate
    second_hour_tshirts = 60 / second_hour_rate
    total_tshirts = first_hour_tshirts + second_hour_tshirts
    result = total_tshirts
    return result

print(solution())