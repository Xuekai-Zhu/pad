def solution():
    """Yanni has $0.85. His mother gave him $0.40 in addition. While going to the mall, Yanni found $0.50.
    He bought a toy that cost $1.6. How much money in cents did Yanni have left?"""
    initial_money = 85 + 40 + 50
    toy_cost = 160
    remaining_money = initial_money - toy_cost
    result = remaining_money
    return result

print(solution())