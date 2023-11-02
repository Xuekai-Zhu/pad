def solution():
    
    sandwiches_on_saturday = 2
    sandwiches_on_sunday = 1
    pieces_of_bread_per_sandwich = 2
    total_pieces_of_bread = (sandwiches_on_saturday + sandwiches_on_sunday) * pieces_of_bread_per_sandwich
    result = total_pieces_of_bread
    return result

print(solution())