def solution():
    num_coloring_books = 2
    coloring_book_price = 4

    num_peanut_packs = 4
    peanut_pack_price = 1.5

    total_paid = 25

    # Calculate the total cost of all items except the stuffed animal
    total_without_stuffed_animal = (num_coloring_books * coloring_book_price) + (num_peanut_packs * peanut_pack_price)

    # Calculate the cost of the stuffed animal
    stuffed_animal_cost = total_paid - total_without_stuffed_animal

    result = stuffed_animal_cost
    return result

print(solution())