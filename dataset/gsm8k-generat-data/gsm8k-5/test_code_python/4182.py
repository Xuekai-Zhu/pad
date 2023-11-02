def solution():
    # Calculate initial number of cantaloupes and honeydews
    initial_cantaloupes = 30
    initial_honeydews = 27

    # Calculate number of cantaloupes and honeydews after some were dropped/rotten
    dropped_cantaloupes = 2
    rotten_honeydews = 3
    remaining_cantaloupes = 8
    remaining_honeydews = 9

    final_cantaloupes = initial_cantaloupes - dropped_cantaloupes - remaining_cantaloupes
    final_honeydews = initial_honeydews - rotten_honeydews - remaining_honeydews

    # Calculate total amount of money made
    cantaloupe_price = 2
    honeydew_price = 3
    total_cantaloupe_sales = (initial_cantaloupes - final_cantaloupes) * cantaloupe_price
    total_honeydew_sales = (initial_honeydews - final_honeydews) * honeydew_price

    total_sales = total_cantaloupe_sales + total_honeydew_sales
    result = total_sales
    return result

print(solution())