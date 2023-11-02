def solution():
    # Define the regular number of each cake
    regular_cheesecakes = 6
    regular_muffins = 5
    regular_red_velvet_cakes = 8

    # Calculate the triple number of each cake
    triple_cheesecakes = regular_cheesecakes * 3
    triple_muffins = regular_muffins * 3
    triple_red_velvet_cakes = regular_red_velvet_cakes * 3

    # Calculate the total number of each cake for the week
    total_cheesecakes = triple_cheesecakes - regular_cheesecakes
    total_muffins = triple_muffins - regular_muffins
    total_red_velvet_cakes = triple_red_velvet_cakes - regular_red_velvet_cakes

    # Calculate the total number of cakes for the week
    total_cakes = total_cheesecakes + total_muffins + total_red_velvet_cakes

    result = total_cakes
    return result

print(solution())