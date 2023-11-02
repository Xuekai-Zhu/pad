def solution():
    """Barry, Thomas and Emmanuel are to share a jar of 200 jelly beans. If Thomas takes 10%, and Barry and Emmanuel are to share the remainder in the ratio 4:5 respectively, how many jelly beans will Emmanuel get?"""
    # Determine how many jelly beans Thomas takes
    thomas_share = 0.1 * 200

    # Determine how many jelly beans are leftover
    leftover = 200 - thomas_share

    # Determine the total ratio between Barry and Emmanuel
    total_ratio = 4 + 5

    # Determine how many parts are assigned to Emmanuel in the ratio
    emmanuel_parts = 5 / total_ratio

    # Determine how many jelly beans Emmanuel gets
    emmanuel_share = emmanuel_parts * leftover

    # Display the number of jelly beans Emmanuel gets
    result = emmanuel_share
    return result

print(solution())