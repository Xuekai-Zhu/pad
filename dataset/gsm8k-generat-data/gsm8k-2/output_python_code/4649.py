def solution():
    """Sally eats 2 sandwiches on Saturday and 1 sandwich on Sunday. If each sandwich uses 2 pieces of bread, how many pieces of bread does Sally eat across Saturday and Sunday?"""
    saturday_sandwiches = 2
    sunday_sandwiches = 1
    pieces_of_bread_per_sandwich = 2
    total_pieces_of_bread = (saturday_sandwiches + sunday_sandwiches) * pieces_of_bread_per_sandwich
    result = total_pieces_of_bread
    return result

print(solution())