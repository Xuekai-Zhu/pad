def solution():
    """Adrianna has 10 pieces of gum to share with her friends. There wasn't enough gum for all her friends, so she went to the store to get 3 more pieces of gum. She gave out gum to 11 friends. How many pieces of gum does Adrianna have now?"""
    initial_gum = 10
    additional_gum = 3
    total_gum = initial_gum + additional_gum
    friends = 11
    gum_given_away = friends * 1
    remaining_gum = total_gum - gum_given_away
    result = remaining_gum
    return result

print(solution())