def solution():
    """At Kaleb's Restaurant, a group with six adults and two children came in to eat. If each adult meal cost six dollars and each children's meal was $4, and every person ordered a soda for $2  how much was the bill?"""
    # Define the prices of adult and children meals, and sodas
    ADULT_MEAL_PRICE = 6
    CHILD_MEAL_PRICE = 4
    SODA_PRICE = 2

    # Define the number of adults and children
    num_adults = 6
    num_children = 2

    # Calculate the costs of adult and children meals, and sodas
    adult_meal_cost = num_adults * ADULT_MEAL_PRICE
    children_meal_cost = num_children * CHILD_MEAL_PRICE
    soda_cost = (num_adults + num_children) * SODA_PRICE

    # Calculate the total bill
    total_bill = adult_meal_cost + children_meal_cost + soda_cost

    # Return the result
    result = total_bill
    return result

print(solution())