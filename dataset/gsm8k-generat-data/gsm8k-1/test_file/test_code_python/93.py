def solution():
    """When Freda cooks canned tomatoes into sauce, they lose half their volume. Each 16 ounce can of tomatoes that she uses contains three tomatoes. Freda’s last batch of tomato sauce made 32 ounces of sauce. How many tomatoes did Freda use?"""
    ounces_of_sauce = 32
    tomatoes_per_can = 3
    ounces_per_can = 16
    total_cans = ounces_of_sauce / (ounces_per_can / 2)
    total_tomatoes = total_cans * tomatoes_per_can
    result = total_tomatoes
    return result

print(solution())