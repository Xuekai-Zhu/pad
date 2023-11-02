def solution():
    # Calculate the total number of hot dogs sold to make $200
    total_hotdogs_sold = 200 / 2 * 10 # Each hot dog sells for $2 and the stand sells 10 hot dogs per hour
    # Calculate the number of hours needed to sell the total hot dogs
    hours_needed = total_hotdogs_sold / 10 
    result = hours_needed
    return result

print(solution())