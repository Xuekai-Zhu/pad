def solution():
    regular_cheesecakes = 6
    regular_muffins = 5
    regular_red_velvet_cakes = 8

    tripled_cheesecakes = regular_cheesecakes * 3
    tripled_muffins = regular_muffins * 3
    tripled_choco_moist_cakes = tripled_cheesecakes + tripled_muffins
    tripled_red_velvet_cakes = regular_red_velvet_cakes * 3

    extra_cheesecakes = tripled_cheesecakes - regular_cheesecakes
    extra_muffins = tripled_muffins - regular_muffins
    extra_red_velvet_cakes = tripled_red_velvet_cakes - regular_red_velvet_cakes
    extra_cakes = extra_cheesecakes + extra_muffins + extra_red_velvet_cakes

    result = extra_cakes
    return result

print(solution())