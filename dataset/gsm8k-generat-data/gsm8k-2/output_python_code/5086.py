def solution():
    """Carter usually bakes 6 cheesecakes, 5 muffins, and 8 red velvet cakes regularly for a week. For this week he was able to bake triple the number of cheesecakes, muffins, chocolate moist cakes, and red velvet cakes. How much more cakes was Carter able to bake for this week?"""
    regular_cheesecakes = 6
    regular_muffins = 5
    regular_red_velvet_cakes = 8
    triple_cheesecakes = 3 * regular_cheesecakes
    triple_muffins = 3 * regular_muffins
    triple_red_velvet_cakes = 3 * regular_red_velvet_cakes
    total_regular_cakes = regular_cheesecakes + regular_muffins + regular_red_velvet_cakes
    total_triple_cakes = triple_cheesecakes + triple_muffins + triple_red_velvet_cakes
    additional_cakes = total_triple_cakes - total_regular_cakes
    result = additional_cakes
    return result

print(solution())