def solution():
    # Define the number of licks each person takes
    dan_licks = 58
    michael_licks = 63
    sam_licks = 70
    david_licks = 70
    lance_licks = 39

    # Calculate the total number of licks
    total_licks = dan_licks + michael_licks + sam_licks + david_licks + lance_licks

    # Calculate the average number of licks
    average_licks = total_licks / 5
    result = average_licks
    return result

print(solution())