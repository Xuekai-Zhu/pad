def solution():
    # Calculate the amount spent on school supplies
    school_supplies_cost = 400/4

    # Calculate the amount left after buying school supplies
    left_after_school_supp = 400 - school_supplies_cost

    # Calculate the amount spent on food for faculty
    food_cost = left_after_school_supp/2

    # Calculate the final amount left
    final_left = left_after_school_supp - food_cost
    result = final_left
    return result

print(solution())