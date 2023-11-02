def solution():
    pieces_per_shepherd_pie = 4
    pieces_per_chicken_pot_pie = 5
    total_pieces_ordered_shepherd_pie = 52
    total_pieces_ordered_chicken_pot_pie = 80
    total_pies_sold_shepherd_pie = total_pieces_ordered_shepherd_pie / pieces_per_shepherd_pie
    total_pies_sold_chicken_pot_pie = total_pieces_ordered_chicken_pot_pie / pieces_per_chicken_pot_pie
    total_pies_sold = total_pies_sold_shepherd_pie + total_pies_sold_chicken_pot_pie
    result = total_pies_sold
    
    return result

print(solution())