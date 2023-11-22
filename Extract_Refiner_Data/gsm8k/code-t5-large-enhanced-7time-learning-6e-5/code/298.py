def solution():
    
    # Define the initial amount of money Annika brought
    initial_money = 50

    # Calculate the amount spent on food and snacks
    food_and_snacks_cost = initial_money / 2

    # Calculate the amount spent on rides
    rides_cost = 10

    # Calculate the total amount spent
    total_spent = food_and_snacks_cost + rides_cost

    # Calculate the amount left
    amount_left = initial_money - total_spent

    # Display the amount left
    result = amount_left
    return result

print(solution())