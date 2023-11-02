def solution():
    georgia_coughs_per_minute = 5
    robert_coughs_per_minute = georgia_coughs_per_minute * 2

    total_coughs = (georgia_coughs_per_minute + robert_coughs_per_minute) * 20
    result = total_coughs
    return result

print(solution())