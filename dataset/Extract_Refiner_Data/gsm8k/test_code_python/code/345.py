def solution():
    
    # Define the cost of each item per month
    FOOD_COST = 25
    TREAT_COST = 20
    Medicine_COST = 100

    # Define the number of weeks in a month
    WEEKS_IN_MONTH = 4

    # Calculate the total cost of the food and treats per month
    food_total = FOOD_COST * WEEKS_IN_MONTH
    treat_total = TREAT_COST * WEEKS_IN_MONTH

    # Calculate the total cost of the medicine per month
    medicine_total = Medicine_COST * WEEKS_IN_MONTH

    # Calculate the total cost of the dog per month
    total_cost = food_total + treat_total + medicine_total

    # Calculate the total cost of the dog per year
    total_yearly_cost = total_cost * 12

    # Display the total cost per year
    result = total_yearly_cost
    return result

print(solution())