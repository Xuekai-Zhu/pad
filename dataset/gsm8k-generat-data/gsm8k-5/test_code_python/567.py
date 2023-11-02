def solution():
    original_price = 2  # The original selling price of the water bottles was $2 each
    reduced_price = 1.85  # Lilith had to reduce the price to $1.85 to sell the water bottles
    dozens = 5  # Lilith had five dozen water bottles to sell
    total_bottles = dozens * 12  # Calculate the total number of water bottles
    original_total = original_price * total_bottles  # Calculate the original total amount of money Lilith would've made
    reduced_total = reduced_price * total_bottles  # Calculate the reduced total amount of money Lilith will make

    # Calculate the amount of money Lilith needs to buy her friend the birthday gift
    gift_price = 15  # Assume the gift costs $15
    total_required = gift_price + (original_total - reduced_total)
    result = total_required
    return result

print(solution())