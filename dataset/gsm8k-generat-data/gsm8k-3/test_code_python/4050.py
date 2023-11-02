def solution():
    """Angus, Patrick, and Ollie went fishing for trout on Rainbow Lake. Angus caught 4 more fish than Patrick did, but Ollie caught 7 fewer fish than Angus. If Ollie caught 5 fish, how many fish did Patrick catch?"""
    # Define Ollie's number of fish caught
    ollie_fish = 5

    # Calculate Angus's number of fish caught
    angus_fish = ollie_fish + 7

    # Calculate Patrick's number of fish caught
    patrick_fish = angus_fish - 4

    # Display Patrick's number of fish caught
    result = patrick_fish
    return result

print(solution())