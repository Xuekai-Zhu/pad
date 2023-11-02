def solution():
    # Define weights of papers
    weekday_weight = 8
    sunday_weight = 2 * weekday_weight

    # Calculate total weight of papers not delivered
    total_weight = ((6 * 250 * weekday_weight) + (1 * 250 * sunday_weight)) * 7 * 10

    # Convert weight to tons and calculate total earnings
    total_earnings = (total_weight / 16) * 20
    result = total_earnings
    return result

print(solution())