def solution():
    muffins_sold_morning = 12
    muffins_sold_afternoon = 4
    muffins_goal = 20
    muffins_left_to_sell = muffins_goal - (muffins_sold_morning + muffins_sold_afternoon)
    result = muffins_left_to_sell
    return result

print(solution())