def solution():
    # Calculate the weight of the small apple Irene shares with her dog every day
    apple_weight = (1/4) * (1/2)  # half of a small apple weighs 1/8 of a pound

    # Calculate the total weight of apples that Irene needs for 2 weeks (14 days)
    total_weight = apple_weight * 14  

    # Calculate the total cost of the apples Irene needs for 2 weeks
    cost = total_weight * 2.00  # apples cost $2.00 a pound

    result = cost
    return result

print(solution())