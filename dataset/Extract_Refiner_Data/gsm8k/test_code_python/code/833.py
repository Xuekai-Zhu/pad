def solution():
    
    # Define the initial cost of the laptop and the discount
    initial_cost = 600
    discount = 200

    # Calculate the new cost after the discount
    new_cost = initial_cost - discount

    # Calculate the total amount Erika has saved
    total_saved = new_cost + 150 - 80

    # Add the extra $50 Erika needs to buy the laptop
    total_saved += 50

    # Display the total amount Erika has saved
    result = total_saved
    return result

print(solution())