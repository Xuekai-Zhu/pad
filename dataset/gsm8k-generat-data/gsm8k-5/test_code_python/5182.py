def solution():
    num_wands_bought = 3  # Kate bought 3 wands
    num_friends = 2  # Kate sold 2 wands to her friends
    sale_price_diff = 5  # Kate sold the wands for $5 more than she paid
    total_sale_price = 130  # Kate collected $130 after the sale

    # Calculate the cost of each wand
    cost_per_wand = (total_sale_price / num_friends) - sale_price_diff

    result = cost_per_wand
    return result

print(solution())