def solution():
    
    # Define the initial amount of money
    initial_money = 18

    # Add the $5 to the share
    initial_money += 5

    # Add the $10 to the share
    initial_money += 10

    # Subtract the $8 spent from the total
    total_money -= 8

    # Triple the remaining amount
    final_money = total_money * 3

    # Display the final amount of money
    result = final_money
    return result

print(solution())