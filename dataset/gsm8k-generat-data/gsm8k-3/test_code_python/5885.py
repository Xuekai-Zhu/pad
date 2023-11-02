def solution():
    """As Dan is learning to screen-print t-shirts to sell at the craft fair, he makes t-shirts, over the first hour, at the rate of one every 12 minutes. Then, in the second hour, he makes one at the rate of every 6 minutes. How many t-shirts does he make over the course of those two hours?"""
    # Calculate the number of t-shirts made in the first hour
    shirts_hour1 = 60 // 12
    # Calculate the number of t-shirts made in the second hour
    shirts_hour2 = 60 // 6
    # Calculate the total number of t-shirts made in two hours
    total_shirts = shirts_hour1 + shirts_hour2
    result = total_shirts
    return result

print(solution())