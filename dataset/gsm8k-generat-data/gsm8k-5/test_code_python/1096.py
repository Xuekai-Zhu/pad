def solution():
    gigi_jellybeans = 15  # Gigi has 15 jellybeans
    rory_jellybeans = gigi_jellybeans + 30  # Rory has 30 more jellybeans than Gigi
    total_jellybeans = gigi_jellybeans + rory_jellybeans  # Total number of jellybeans between Gigi and Rory
    lorelai_jellybeans = 3 * total_jellybeans  # Lorelai ate three times the total number of jellybeans

    result = lorelai_jellybeans
    return result

print(solution())