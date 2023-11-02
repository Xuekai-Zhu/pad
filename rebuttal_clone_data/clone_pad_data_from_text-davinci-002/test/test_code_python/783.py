def solution():
     num_pots = 60
     num_pots_vertical = 5
     num_pots_horizontal = 3
     num_shelves_needed = num_pots / (num_pots_vertical * num_pots_horizontal)
     result = num_shelves_needed
     return result

print(solution())