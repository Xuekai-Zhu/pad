def solution():
    """Mary and Rose went shopping to buy presents. They spent the same amount. Mary bought two pairs of sunglasses for $50 each and a pair of jeans for $100. Rose bought a pair of shoes at $150 and two decks of basketball cards. How much did one deck of basketball cards cost?"""
    # Define the total amount spent by Mary
    mary_total = (50 * 2) + 100

    # Define the total amount spent by Rose
    rose_total = 150 + (2 * deck_price)

    # Set the two totals equal to each other and solve for deck price
    deck_price = (mary_total - 150) / 2

    result = deck_price
    return result

print(solution())