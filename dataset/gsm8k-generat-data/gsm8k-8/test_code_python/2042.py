def solution():
    saved_money = 400

    # Calculate the amount spent on school supplies
    school_supplies = saved_money / 4

    # Calculate the amount left after buying school supplies
    money_after_supplies = saved_money - school_supplies

    # Calculate the amount spent on food for faculty
    faculty_food = money_after_supplies / 2

    # Calculate the amount of money left after buying faculty food
    money_left = money_after_supplies - faculty_food
    result = money_left
    return result

print(solution())