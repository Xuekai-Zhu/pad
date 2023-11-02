def solution():
    """Peggy fell off her bike and skinned her knees. She needed two bandages on her left knee and three bandages on her right knee. If the box of bandages had 8 less than two dozen bandages before Peggy skinned her knees, how many bandages were left in the box after Peggy finished putting bandages on her knees?"""
    # Calculate the total number of bandages Peggy used
    total_bandages = 2 + 3

    # Calculate the number of bandages in two dozen minus 8
    bandages_initial = 2 * 12 - 8

    # Calculate the number of bandages left in the box
    bandages_left = bandages_initial - total_bandages

    # Return the result
    result = bandages_left
    return result

print(solution())