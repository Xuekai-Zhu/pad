def solution():
    """If 8 carpenters can make 50 chairs in 10 days, how many carpenters are needed to make 75 chairs in 10 days?"""
    # Define the initial number of carpenters and chairs per day
    initial_carpenters = 8
    initial_chairs_per_day = 50 / 10

    # Calculate the number of carpenters needed to make 75 chairs in 10 days
    chairs_per_day = 75 / 10
    carpenters_needed = (chairs_per_day / initial_chairs_per_day) * initial_carpenters

    # Display the number of carpenters needed
    result = carpenters_needed
    return result

print(solution())