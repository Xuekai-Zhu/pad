def solution():
    """Sofia and her mother go to the grocery store and buys 10kgs of oranges to be used in their home for the week. While at the store, Sofia's father calls and says they're to add 5 more kgs since their neighbor also wanted some supplies. When they reach home, they estimated that for the next coming two weeks they'll have to buy twice as many oranges each week for the supplies to be enough. What the total quantity of oranges they would have bought after the three weeks."""
    initial_quantity = 10
    additional_quantity = 5
    total_quantity = initial_quantity + additional_quantity
    two_week_quantity = total_quantity * 2
    total_quantity += two_week_quantity
    result = total_quantity
    return result

print(solution())