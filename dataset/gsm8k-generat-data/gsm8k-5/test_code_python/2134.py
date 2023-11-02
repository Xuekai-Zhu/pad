def solution():
    cans_martha = 90  # Martha collected 90 cans
    cans_diego = (1/2)*cans_martha + 10  # Diego collected 10 more than half of Martha's cans
    total_cans = cans_martha + cans_diego  # Total cans collected by both

    # Calculate how many more cans they need to collect to reach their goal of 150 cans
    remaining_cans = 150 - total_cans
    result = remaining_cans
    return result

print(solution())