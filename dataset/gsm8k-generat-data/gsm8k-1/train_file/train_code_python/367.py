def solution():
    """Linda bought two coloring books at $4 each, 4 packs of peanuts at $1.50 each pack, and one stuffed animal. She gave the cashier $25 and got no change. How much does a stuffed animal cost?"""
    coloring_book_cost = 4 * 2
    peanuts_cost = 1.5 * 4
    total_cost = coloring_book_cost + peanuts_cost
    stuffed_animal_cost = 25 - total_cost
    result = stuffed_animal_cost
    return result

print(solution())