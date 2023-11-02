def solution():
    """Dan can get to the center of a lollipop in 58 licks.  Micheal does it in 63 licks.  Sam & David each take 70 licks to get to the center of a lollipop while Lance only needs 39 licks.  What is the average amount of licks it takes to get to the center of a lollipop?"""
    # Define the number of licks it takes for each person to get to the center of a lollipop
    dan = 58
    michael = 63
    sam = 70
    david = 70
    lance = 39

    # Calculate the average number of licks
    average = (dan + michael + sam + david + lance) / 5

    # Display the average number of licks
    result = average
    return result

print(solution())