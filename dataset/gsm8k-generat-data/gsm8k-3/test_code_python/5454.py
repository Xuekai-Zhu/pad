def solution():
    """Maria collects stamps and wants to enlarge her collection. She has collected 40 stamps so far and plans to have 20% more. How many stamps in total does Maria want to collect?"""
    # Define the initial number of stamps
    initial_stamps = 40

    # Define the percentage increase
    percentage_increase = 20

    # Calculate the total number of stamps Maria wants to collect
    total_stamps = initial_stamps + (initial_stamps * (percentage_increase/100))

    # Display the total number of stamps
    result = total_stamps
    return result

print(solution())