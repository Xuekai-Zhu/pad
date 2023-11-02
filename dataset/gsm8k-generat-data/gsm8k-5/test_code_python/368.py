def solution():
    # Calculate the total cost of the coloring books
    coloring_book_cost = 2 * 4  # Linda bought two coloring books at $4 each

    # Calculate the total cost of the peanuts
    peanut_cost = 4 * 1.5  # Linda bought 4 packs of peanuts at $1.50 each pack

    # Calculate the total cost of the purchase
    total_cost = coloring_book_cost + peanut_cost  # Does not include the cost of the stuffed animal

    # Calculate the cost of the stuffed animal
    stuffed_animal_cost = 25 - total_cost  # Linda gave the cashier $25 and got no change

    result = stuffed_animal_cost
    return result

print(solution())