def solution():
    # Calculate the total number of apples Bella eats in a week
    weekly_consumption = 6 * 7  # Bella eats 6 apples a day for 7 days
    weekly_share = weekly_consumption / 3  # Grace consumes a third of the apples Bella eats

    # Calculate the total number of apples Grace will have after 6 weeks
    total_apples = weekly_share * 6  # Grace has the same number of apples each week for 6 weeks
    result = total_apples
    return result

print(solution())