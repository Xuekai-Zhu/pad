def solution():
    goal = 20
    sold_morning = 12
    sold_afternoon = 4

    # Calculate the total number of muffins sold so far
    total_sold = sold_morning + sold_afternoon

    # Calculate the number of muffins left to sell to hit the goal
    muffins_left = goal - total_sold
    result = muffins_left
    return result

print(solution())