def solution():
    # Calculate the regular number of cakes Carter bakes in a week
    regular_cheesecakes = 6
    regular_muffins = 5
    regular_red_velvet_cakes = 8
    regular_total_cakes = regular_cheesecakes + regular_muffins + regular_red_velvet_cakes

    # Calculate the tripled number of cakes Carter was able to bake this week
    tripled_cheesecakes = 3 * regular_cheesecakes
    tripled_muffins = 3 * regular_muffins
    tripled_red_velvet_cakes = 3 * regular_red_velvet_cakes
    tripled_total_cakes = tripled_cheesecakes + tripled_muffins + tripled_red_velvet_cakes

    # Calculate how much more cakes Carter baked this week
    more_cakes = tripled_total_cakes - regular_total_cakes
    result = more_cakes
    return result

print(solution())