def solution():
    num_phones = 3  # Melinda, Zoe and Joel want to buy 3 iPhones
    price_per_phone = 600  # The price of each iPhone is $600

    # Total cost if they purchase individually
    total_cost_individual = num_phones * price_per_phone

    # Total cost if they purchase together and get the 5% discount
    total_cost_pooled = (num_phones * price_per_phone) * 0.95

    # Amount saved by purchasing together
    amount_saved = total_cost_individual - total_cost_pooled
    result = amount_saved
    return result

print(solution())