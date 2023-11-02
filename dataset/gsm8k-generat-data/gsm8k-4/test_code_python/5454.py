def solution():
    """Maria collects stamps and wants to enlarge her collection. She has collected 40 stamps so far and plans to have 20% more. How many stamps in total does Maria want to collect?"""
    # Define the number of stamps Maria has collected so far
    collected_stamps = 40

    # Calculate the percentage increase Maria wants
    percentage_increase = 20 / 100

    # Calculate the number of stamps Maria wants to collect
    total_stamps = collected_stamps + (collected_stamps * percentage_increase)

    # return result
    result = total_stamps
    return result

print(solution())