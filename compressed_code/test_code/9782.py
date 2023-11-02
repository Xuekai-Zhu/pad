def solution():
    
    regular_cheesecakes = 6
    regular_muffins = 5
    regular_red_velvet_cakes = 8
    tripled_cheesecakes = regular_cheesecakes * 3
    tripled_muffins = regular_muffins * 3
    tripled_red_velvet_cakes = regular_red_velvet_cakes * 3
    more_cheesecakes = tripled_cheesecakes - regular_cheesecakes
    more_muffins = tripled_muffins - regular_muffins
    more_red_velvet_cakes = tripled_red_velvet_cakes - regular_red_velvet_cakes
    total_more_cakes = more_cheesecakes + more_muffins + more_red_velvet_cakes
    result = total_more_cakes
    return result

print(solution())