def solution():
    
    # Define the initial amount of money Annika brought to the town fair
    initial_money = 50

    # Calculate the amount spent on food and snacks
    food_snacks = initial_money / 2

    # Calculate the amount spent on rides
    rides = 10

    # Calculate the total amount spent
    total_spent = food_snacks + rides

    # Calculate the amount left
    amount_left = initial_money - total_spent

    # Display the amount left
    result = amount_left
    return result

print(solution())