def solution():
 
    animals_seen_Jan = 26
    animals_seen_Feb = animals_seen_Jan * 3
    animals_seen_Mar = animals_seen_Feb / 2
    total_animals_seen = animals_seen_Jan + animals_seen_Feb + animals_seen_Mar
    
    return total_animals_seen

print(solution())