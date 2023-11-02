def solution():
    
    total_mangoes = 560
    sold_mangoes = total_mangoes / 2
    remaining_mangoes = total_mangoes - sold_mangoes
    mangoes_per_neighbor = remaining_mangoes / 8
    result = mangoes_per_neighbor
    return result

print(solution())