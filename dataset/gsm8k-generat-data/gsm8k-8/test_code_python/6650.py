def solution():
    # Calculate the total number of bottles sold from Wednesday to Sunday
    bottles_sold = 50 * 5

    # Calculate the total number of bottles sold during the week
    total_sold = 2445 + 900 + bottles_sold

    # Calculate the number of bottles left in inventory after the week
    inventory = 4500 - total_sold + 650

    result = inventory
    return result

print(solution())