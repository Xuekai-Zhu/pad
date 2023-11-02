def solution():
    """Connor is taking his date to the movies. The tickets cost $10.00 each. They decided to get the large popcorn & 2 drink combo meal for $11.00 and each grab a box of candy for $2.50 each. How much will Connor spend on his date?"""
    ticket_price = 10
    popcorn_drink_combo_price = 11
    candy_price = 2.5
    total_price = (2 * ticket_price) + popcorn_drink_combo_price + (2 * candy_price)
    result = total_price
    return result

print(solution())