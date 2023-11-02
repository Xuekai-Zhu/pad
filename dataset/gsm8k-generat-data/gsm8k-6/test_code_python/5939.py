def solution():
    # Find the total number of cans collected in 5 days
    total_cans = 20 + (5 * 4)  # starts with 20 cans, increases by 5 each day for 4 days

    # Find the average number of cans collected per day
    average_cans = total_cans / 5  # collected for 5 days

    result = average_cans
    return result

print(solution())