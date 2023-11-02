def solution():
    # Ken's house is 4 miles away from Dawn's house
    # Dawn's house is half the distance from Mary's as Ken's house
    # Therefore, Mary's house is 2 miles away from Dawn's house

    # Ken first goes from his house to Dawn's house (4 miles)
    # Then he goes from Dawn's house to Mary's house (2 miles)
    # Then he goes from Mary's house back to Dawn's house (2 miles)
    # Finally, he goes from Dawn's house back to his own house (4 miles)

    # Total distance covered by Ken
    total_distance = 4 + 2 + 2 + 4

    result = total_distance
    return result

print(solution())