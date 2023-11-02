def solution():
    """Luna's monthly food budget is equal to 60% of her house rental budget while her phone bill budget is 10% of her food budget. If the total budget of house rental and food budget is $240, how much is Luna's total monthly budget to pay all those expenses?"""
    # Define the percentage of the house rental budget that goes to the food budget
    FOOD_PERCENTAGE = 0.6

    # Calculate the house rental budget
    house_rental_budget = 240 / (1 + FOOD_PERCENTAGE)

    # Calculate the food budget
    food_budget = FOOD_PERCENTAGE * house_rental_budget

    # Calculate the phone bill budget
    phone_bill_budget = 0.1 * food_budget

    # Calculate the total monthly budget
    total_budget = house_rental_budget + food_budget + phone_bill_budget

    # Display the total monthly budget
    result = total_budget
    return result

print(solution())