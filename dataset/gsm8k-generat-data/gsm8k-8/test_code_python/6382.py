def solution():
    # Calculate the total number of children
    total_children = 14 + 16 + 12 + (14 + 16 + 12) / 2

    # Calculate the total number of bottles needed per day
    total_bottles_per_day = total_children * 3

    # Calculate the total number of bottles needed for the entire camp
    total_bottles = total_bottles_per_day * 3

    # Calculate the total number of bottles in the purchased cases
    purchased_cases = 13
    total_bottles_purchased = purchased_cases * 24

    # Calculate the remaining number of bottles needed to be purchased
    remaining_bottles = total_bottles - total_bottles_purchased
    result = remaining_bottles
    return result

print(solution())