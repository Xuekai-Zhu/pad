def solution():
    """Yanni has $0.85. His mother gave him $0.40 in addition. While going to the mall, Yanni found $0.50. He bought a toy that cost $1.6. How much money in cents did Yanni have left?"""
    # Define the initial amount of money Yanni has
    initial_money = 85

    # Add the amount of money Yanni's mother gave him
    initial_money += 40

    # Add the amount of money Yanni found
    initial_money += 50

    # Subtract the cost of the toy
    remaining_money = initial_money - 160

    # Display the amount of money Yanni has left, in cents
    result = remaining_money
    return result

print(solution())