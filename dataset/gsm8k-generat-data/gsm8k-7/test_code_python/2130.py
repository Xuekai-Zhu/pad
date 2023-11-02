def solution():
    total_budget = 60
    first_course_price = 15
    second_course_price = first_course_price + 5
    dessert_price = second_course_price * 0.25

    # Calculate the total cost of Amelia's meals
    total_cost = first_course_price + second_course_price + dessert_price

    # Calculate the amount left in Amelia's budget after buying all her meals
    remaining_budget = total_budget - total_cost
    result = remaining_budget
    return result

print(solution())