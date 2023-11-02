def solution():
    """Sally Draper gave her dad Don Draper 10oz of rum on his pancakes. Don can consume a maximum of 3 times that amount of rum for a healthy diet. If he already had 12oz of rum earlier that day, how many oz of rum can Don have after eating all of the rum and pancakes?"""
    # Define the amount of rum Sally gave to Don
    sally_rum = 10

    # Define the maximum amount of rum Don can consume
    max_rum = sally_rum * 3

    # Define the amount of rum Don had earlier that day
    earlier_rum = 12

    # Calculate the total amount of rum Don can consume in a day
    total_max_rum = max_rum + earlier_rum

    # Calculate the remaining amount of rum Don can consume after eating the rum and pancakes
    remaining_rum = total_max_rum - sally_rum

    # Display the remaining amount of rum Don can consume
    result = remaining_rum
    return result

print(solution())