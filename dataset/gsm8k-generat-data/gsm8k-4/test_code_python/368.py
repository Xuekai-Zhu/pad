def solution():
    """Linda bought two coloring books at $4 each, 4 packs of peanuts at $1.50 each pack, and one stuffed animal. She gave the cashier $25 and got no change. How much does a stuffed animal cost?"""
    # Define the prices of coloring books and packs of peanuts
    coloring_book_price = 4
    peanuts_price = 1.5
    stuffed_animal_price = None

    # Calculate the total cost of coloring books and packs of peanuts
    total_cost = (2 * coloring_book_price) + (4 * peanuts_price)

    # Calculate the price of the stuffed animal
    stuffed_animal_price = 25 - total_cost

    result = stuffed_animal_price
    return result

print(solution())