def solution():
    """Adam went to a store to buy some sweets. He bought 7 candies of type A and 10 candies of type B. One candy of type A costs $0.5, and one candy of type B costs $0.75. How much change did Adam get, if he paid the cashier $15?"""
    candy_a_cost = 0.5
    candy_b_cost = 0.75
    candy_a_count = 7
    candy_b_count = 10
    total_cost = (candy_a_cost * candy_a_count) + (candy_b_cost * candy_b_count)
    paid_amount = 15
    change = paid_amount - total_cost
    result = change
    return result

print(solution())