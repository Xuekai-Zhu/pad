def solution():
    """A store sold a certain brand of jeans for $40.
    They only have few pairs of jeans left so they decided to give 10% discount on every two pairs of jeans bought by a customer at any one time.
    How much will a customer pay for 3 pairs of jeans?"""
    # Define the price per pair of jeans
    PRICE_PER_PAIR = 40

    # Define the discount rate for every two pairs of jeans
    DISCOUNT_RATE = 0.1

    # Calculate the total cost of 3 pairs of jeans without discount
    total_cost_without_discount = 3 * PRICE_PER_PAIR

    # Calculate the number of pairs of jeans with the discount
    num_pairs_with_discount = 3 // 2

    # Calculate the total cost of pairs with discount
    total_cost_with_discount = num_pairs_with_discount * (PRICE_PER_PAIR * 2) * (1 - DISCOUNT_RATE)

    # Calculate the total cost of all pairs of jeans
    total_cost = total_cost_with_discount + (total_cost_without_discount % (PRICE_PER_PAIR * 2))

    # Display the total cost
    result = total_cost
    return result

print(solution())