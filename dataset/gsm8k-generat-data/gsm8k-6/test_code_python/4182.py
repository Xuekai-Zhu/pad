def solution():
    # Calculate the number of cantaloupes and honeydews sold
    starting_cantaloupes = 30
    starting_honeydews = 27
    dropped_cantaloupes = 2
    rotten_honeydews = 3
    ending_cantaloupes = 8
    ending_honeydews = 9
    sold_cantaloupes = starting_cantaloupes - ending_cantaloupes + dropped_cantaloupes
    sold_honeydews = starting_honeydews - ending_honeydews + rotten_honeydews
    # Calculate the total amount of money made
    cantaloupe_sales = sold_cantaloupes * 2
    honeydew_sales = sold_honeydews * 3
    total_sales = cantaloupe_sales + honeydew_sales
    result = total_sales
    return result

print(solution())