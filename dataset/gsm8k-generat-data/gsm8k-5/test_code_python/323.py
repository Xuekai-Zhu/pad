def solution():
    total_guests = 22 + 36  # Jay and Gloria invited a total of 58 guests
    total_flags_needed = total_guests + 2  # They need flags for all the guests and 1 for each of them

    # Calculate the total number of flag packs needed (each pack has 5 flags)
    flag_packs_needed = total_flags_needed / 5
    if flag_packs_needed % 1 != 0:  # If the division has a remainder, round up to the nearest whole number of packs
        flag_packs_needed = int(flag_packs_needed) + 1
    else:
        flag_packs_needed = int(flag_packs_needed)

    # Calculate the total cost of the flags (each pack costs $1.00)
    total_cost = flag_packs_needed * 1.00
    result = total_cost
    return result

print(solution())