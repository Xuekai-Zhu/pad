def solution():
    num_bottles = 5 * 12
    original_price = 2
    reduced_price = 1.85
    gift_cost = original_price * num_bottles  # The cost of the gift if Lilith sold all bottles at the original price
    revenue = reduced_price * num_bottles  # The total amount of money Lilith earns from selling all bottles at the reduced price
    profit = revenue - gift_cost  # The profit Lilith makes after selling all bottles at the reduced price
    result = gift_cost - profit  # The total amount of money Lilith needs to buy the birthday gift after selling all bottles at the reduced price
    return result

print(solution())