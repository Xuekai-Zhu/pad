def solution():
    people_in_house = 15
    people_eating_pizza = people_in_house * (3/5)
    pizza_pieces_each = 4
    pizza_pieces_left = people_eating_pizza * pizza_pieces_each - 50
    
    return pizza_pieces_left

print(solution())