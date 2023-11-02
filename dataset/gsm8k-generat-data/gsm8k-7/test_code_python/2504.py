def solution():
    refills = 0
    used_up = 0
    ending_wipes = 60

    # Calculate the number of refills Elsie made throughout the day
    while ending_wipes <= 100:
        refills += 1
        used_up += 20
        ending_wipes += 10

    # Calculate the number of wipes Elsie still had in the container in the morning
    starting_wipes = ending_wipes + used_up
    result = starting_wipes
    return result

print(solution())