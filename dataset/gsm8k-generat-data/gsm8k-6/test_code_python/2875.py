def solution():
    # Calculate the distance between Ken's house and Mary's house
    distance_Ken_Mary = 4 * 2   # Ken's house is twice as far from Mary's house, and Ken's house is 4 miles away from Dawn's house

    # Calculate the total distance Ken will cover
    total_distance = (4 + distance_Ken_Mary + 4 + distance_Ken_Mary + 4)  # Ken goes from his house to Dawn's house, then Mary's, then back to Dawn's before going back to his own house
    result = total_distance
    return result

print(solution())