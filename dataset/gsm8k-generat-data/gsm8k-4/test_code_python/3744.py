def solution():
    """Sally Draper gave her dad Don Draper 10oz of rum on his pancakes. Don can consume a maximum of 3 times that amount of rum for a healthy diet. If he already had 12oz of rum earlier that day, how many oz of rum can Don have after eating all of the rum and pancakes?"""
    # Define the maximum amount of rum Don can consume for a healthy diet
    max_rum_consumption = 10 * 3

    # Calculate the total amount of rum consumed after eating the pancakes
    total_rum_consumed = 10 + 12

    # Calculate the remaining amount of rum Don can consume for a healthy diet
    remaining_rum = max_rum_consumption - total_rum_consumed

    # Return the result
    result = remaining_rum
    return result

print(solution())