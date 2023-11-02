def solution():
    """Carter usually bakes 6 cheesecakes, 5 muffins, and 8 red velvet cakes regularly for a week. For this week he was able to bake triple the number of cheesecakes, muffins, chocolate moist cakes, and red velvet cakes. How much more cakes was Carter able to bake for this week?"""
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