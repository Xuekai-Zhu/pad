def solution():
    """Yanni has $0.85. His mother gave him $0.40 in addition. While going to the mall, Yanni found $0.50. He bought a toy that cost $1.6. How much money in cents did Yanni have left?"""
    # Define the initial amount of money
    initial_money = 85

    # Add the money given by Yanni's mother
    initial_money += 40

    # Add the money Yanni found
    initial_money += 50

    # Subtract the cost of the toy
    initial_money -= 160

    # Convert the result to cents
    cents_left = initial_money

    # Return the result
    result = cents_left
    return result

print(solution())