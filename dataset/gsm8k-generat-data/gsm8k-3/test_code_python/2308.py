def solution():
    """Peggy fell off her bike and skinned her knees.  She needed two bandages on her left knee and three bandages on her right knee.  If the box of bandages had 8 less than two dozen bandages before Peggy skinned her knees, how many bandages were left in the box after Peggy finished putting bandages on her knees?"""
    
    # Calculate the total number of bandages Peggy used
    total_bandages = 2 + 3

    # Calculate the total number of bandages in a dozen
    dozen_bandages = 12

    # Calculate the total number of bandages in two dozen
    two_dozen = 2 * dozen_bandages

    # Calculate the number of bandages in the box before Peggy used any
    initial_bandages = two_dozen - 8

    # Calculate the number of bandages left in the box after Peggy used some
    bandages_left = initial_bandages - total_bandages

    # Display the number of bandages left in the box
    result = bandages_left
    return result

print(solution())