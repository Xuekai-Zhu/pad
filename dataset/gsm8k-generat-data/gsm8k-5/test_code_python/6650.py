def solution():
    starting_inventory = 4500
    bottles_sold_monday = 2445
    bottles_sold_tuesday = 900
    bottles_sold_rest_of_week = 50 * 5
    bottles_delivered_saturday = 650

    # Calculate the total number of bottles sold during the week
    total_sold = bottles_sold_monday + bottles_sold_tuesday + bottles_sold_rest_of_week

    # Calculate the final inventory after the week
    final_inventory = starting_inventory - total_sold + bottles_delivered_saturday
    result = final_inventory
    return result

print(solution())