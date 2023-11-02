def solution():

    regular_cheesecakes = 6
    regular_muffins = 5
    regular_red_velvet = 8

    this_week_cheesecakes = 3 * regular_cheesecakes
    this_week_muffins = 3 * regular_muffins
    this_week_red_velvet = 3 * regular_red_velvet

    total_regular_cakes = regular_cheesecakes + regular_muffins + regular_red_velvet
    total_this_week_cakes = this_week_cheesecakes + this_week_muffins + this_week_red_velvet

    total_more_cakes = total_this_week_cakes - total_regular_cakes
    return total_more_cakes

print(solution())