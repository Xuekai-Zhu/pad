def solution():
    # Calculate the total number of roses received by Bella
    dozen_of_roses = 2  # Bella received 2 dozen roses from her parents
    roses_from_friends = 2 * 10  # Bella received 2 roses from each of her 10 dancer friends
    total_roses = dozen_of_roses * 12 + roses_from_friends  # convert dozen of roses to individual roses and sum up with roses from friends
    result = total_roses
    return result

print(solution())