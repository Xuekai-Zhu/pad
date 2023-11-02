def solution():
    remaining_months = 3  # There are 3 months left in the year
    current_listens = 60000  # Jordan currently has 60,000 listens
    total_listens = current_listens

    # Double the number of listens per month for the remaining months
    for i in range(remaining_months):
        current_listens *= 2
        total_listens += current_listens

    result = total_listens
    return result

print(solution())