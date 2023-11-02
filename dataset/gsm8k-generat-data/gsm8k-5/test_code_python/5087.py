def solution():
    # Regular number of cakes baked per week
    regular_cheesecakes = 6
    regular_muffins = 5
    regular_red_velvet_cakes = 8

    # Triple the number of cakes baked for this week
    new_cheesecakes = regular_cheesecakes * 3
    new_muffins = regular_muffins * 3
    new_red_velvet_cakes = regular_red_velvet_cakes * 3
    new_chocolate_moist_cakes = new_cheesecakes + new_muffins + new_red_velvet_cakes

    # Calculate the difference in the number of cakes baked
    extra_cheesecakes = new_cheesecakes - regular_cheesecakes
    extra_muffins = new_muffins - regular_muffins
    extra_red_velvet_cakes = new_red_velvet_cakes - regular_red_velvet_cakes
    extra_cakes = extra_cheesecakes + extra_muffins + extra_red_velvet_cakes

    result = extra_cakes
    return result

print(solution())