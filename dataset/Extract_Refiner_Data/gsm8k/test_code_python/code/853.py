def solution():
    
    # Define the initial amount of water passing through the river
    initial_amount = 4000

    # Calculate the amount of water passing through the river after a day of rain
    daily_amount = initial_amount * 2

    # Calculate the amount of water passing through the river after the third day
    final_amount = daily_amount + 6000

    # Display the total amount of water passing through the river
    result = final_amount
    return result

print(solution())