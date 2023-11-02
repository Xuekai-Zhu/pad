def solution():
    num_adults = 6
    adult_meal_price = 6

    num_children = 2
    child_meal_price = 4

    num_people = num_adults + num_children

    soda_price = 2

    # Calculate the total cost of all adult meals
    total_adult_cost = num_adults * adult_meal_price

    # Calculate the total cost of all children's meals
    total_child_cost = num_children * child_meal_price

    # Calculate the total cost of all sodas
    total_soda_cost = num_people * soda_price

    # Calculate the total bill
    total_bill = total_adult_cost + total_child_cost + total_soda_cost
    result = total_bill
    return result

print(solution())