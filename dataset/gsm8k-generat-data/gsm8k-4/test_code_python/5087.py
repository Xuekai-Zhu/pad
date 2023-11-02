def solution():
    """Carter usually bakes 6 cheesecakes, 5 muffins, and 8 red velvet cakes regularly for a week. For this week he was able to bake triple the number of cheesecakes, muffins, chocolate moist cakes, and red velvet cakes. How much more cakes was Carter able to bake for this week?"""
    # Define the regular number of cheesecakes, muffins, and red velvet cakes
    regular_cheesecakes = 6
    regular_muffins = 5
    regular_redvelvet = 8

    # Calculate the tripled number of cheesecakes, muffins, and red velvet cakes
    tripled_cheesecakes = regular_cheesecakes * 3
    tripled_muffins = regular_muffins * 3
    tripled_redvelvet = regular_redvelvet * 3

    # Calculate the total increase in number of cakes
    increase = tripled_cheesecakes + tripled_muffins + tripled_redvelvet - (regular_cheesecakes + regular_muffins + regular_redvelvet)

    # return the result
    result = increase
    return result

print(solution())