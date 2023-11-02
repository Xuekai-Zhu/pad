def solution():
    crayon_packs = 5
    book_packs = 10
    calculator_packs = 3
    cost_of_crayon_packs = 5 * crayon_packs
    cost_of_book_packs = 5 * book_packs
    cost_of_calculator_packs = 5 * calculator_packs
    total_spent = cost_of_crayon_packs + cost_of_book_packs + cost_of_calculator_packs
    cost_of_one_bag = 10
    money_left = 200 - total_spent
    number_of_bags = money_left / cost_of_one_bag
    result = number_of_bags
    return result

print(solution())