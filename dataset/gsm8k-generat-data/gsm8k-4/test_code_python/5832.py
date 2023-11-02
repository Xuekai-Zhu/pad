def solution():
    """Harvey's started out with 25 steaks. Then he sold some, and only had 12 steaks left. He sold 4 more steaks, at 10 dollars. How many steaks did he sell in all?"""
    # Define the initial number of steaks
    initial_steaks = 25

    # Define the number of steaks left after selling some
    steaks_left = 12

    # Calculate the number of steaks sold
    steaks_sold = initial_steaks - steaks_left

    # Add the 4 steaks he sold later
    total_steaks_sold = steaks_sold + 4

    # Return the result
    result = total_steaks_sold
    return result

print(solution())