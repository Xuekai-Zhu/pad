def solution():
    adult_meal_cost = 6
    children_meal_cost = 4
    soda_cost = 2
    number_of_adults = 6
    number_of_children = 2
    total_bill = (adult_meal_cost * number_of_adults) + (children_meal_cost * number_of_children) + (soda_cost * (number_of_adults + number_of_children))
    result = total_bill
    return result

print(solution())