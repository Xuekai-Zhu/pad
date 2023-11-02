def solution():
    num_crayon_packs = 5
    crayon_pack_price = 5

    num_books = 10
    book_price = 5

    num_calculators = 3
    calculator_price = 5

    total_cost = (num_crayon_packs * crayon_pack_price) + (num_books * book_price) + (num_calculators * calculator_price)

    change = 200 - total_cost

    bag_price = 10

    num_bags = change / bag_price
    result = num_bags
    return result

print(solution())