def solution():
    """Kira's cat eats a pound of kibble every 4 hours. Kira fills her cat's bowl with 3 pounds of kibble before going to work. When she returns, Kira weighs the bowl and there is still 1 pound left. How many hours was Kira away from home?"""
    # Define the initial amount of kibble
    initial_kibble = 3

    # Define the amount of kibble left
    kibble_left = 1

    # Define the rate of kibble consumption
    consumption_rate = 1/4

    # Calculate the amount of kibble consumed
    consumed_kibble = initial_kibble - kibble_left

    # Calculate the time Kira was away from home
    time_away = consumed_kibble/consumption_rate

    # Display the time
    result = time_away
    return result

print(solution())