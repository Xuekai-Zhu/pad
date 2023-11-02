def solution():
    """Adrianna has 10 pieces of gum to share with her friends. There wasn't enough gum for all her friends, so she went to the store to get 3 more pieces of gum. She gave out gum to 11 friends. How many pieces of gum does Adrianna have now?"""
    starting_gum = 10
    additional_gum = 3
    friends = 11
    total_gum = starting_gum + additional_gum - friends
    result = total_gum
    return result

print(solution())