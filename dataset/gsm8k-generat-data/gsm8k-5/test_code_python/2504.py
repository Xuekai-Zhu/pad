def solution():
    refills = 0  # Start with no refills
    used_wipes = 0  # Start with no used wipes
    remaining_wipes = 60  # Elsie has 60 wipes left at the end of the day

    # Elsie uses 20 wipes each time before adding 10 more
    while remaining_wipes > 0:
        refills += 1
        used_wipes += 20
        remaining_wipes = remaining_wipes - 10 + 20

    # Calculate the number of wipes in the container in the morning
    initial_wipes = used_wipes - 20 * refills
    result = initial_wipes
    return result

print(solution())