def solution():
    cantaloupe_price = 2
    honeydew_price = 3

    starting_cantaloupes = 30
    starting_honeydews = 27

    dropped_cantaloupes = 2
    rotten_honeydews = 3

    ending_cantaloupes = 8
    ending_honeydews = 9

    # Calculate the total number of cantaloupes sold
    total_cantaloupes_sold = starting_cantaloupes - dropped_cantaloupes - ending_cantaloupes

    # Calculate the total number of honeydews sold
    total_honeydews_sold = starting_honeydews - rotten_honeydews - ending_honeydews

    # Calculate the total revenue from cantaloupes sold
    cantaloupe_revenue = total_cantaloupes_sold * cantaloupe_price

    # Calculate the total revenue from honeydews sold
    honeydew_revenue = total_honeydews_sold * honeydew_price

    # Calculate the total revenue from all sales
    total_revenue = cantaloupe_revenue + honeydew_revenue
    result = total_revenue
    return result

print(solution())