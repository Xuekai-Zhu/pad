def solution():
    price_per_pair = 40  # price of one pair of jeans
    num_pairs = 3  # number of pairs of jeans bought
    num_discounted_pairs = num_pairs//2  # number of pairs eligible for discount
    discounted_price = 0.9 * price_per_pair  # price per discounted pair after 10% discount
    total_price = (num_discounted_pairs * discounted_price) + (num_pairs % 2 * price_per_pair)  # total price for all pairs
    result = total_price
    return result

print(solution())