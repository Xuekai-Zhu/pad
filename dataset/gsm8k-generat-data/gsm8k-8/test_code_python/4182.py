def solution():
    # Define the prices of the melons
    cantaloupe_price = 2
    honeydew_price = 3

    # Calculate the total number of melons at the start of the day
    total_melons_start = 30 + 27

    # Calculate the total number of melons at the end of the day
    dropped_cantaloupes = 2
    rotten_honeydews = 3
    cantaloupes_left = 8
    honeydews_left = 9
    total_melons_end = cantaloupes_left + honeydews_left + dropped_cantaloupes + rotten_honeydews

    # Calculate the total amount of money made
    total_money_made = (30 - cantaloupes_left) * cantaloupe_price + (27 - honeydews_left) * honeydew_price
    result = total_money_made
    return result

print(solution())