def solution():
    """There are 30 pieces of popcorn in a serving. Jared can eat 90 pieces of popcorn and his three other friends can each eat 60 pieces of popcorn. How many servings of popcorn should Jared order for all of them?"""
    jared_popcorn = 90
    other_friends_popcorn = 60 * 3
    total_popcorn_needed = jared_popcorn + other_friends_popcorn
    servings_needed = total_popcorn_needed / 30
    result = servings_needed
    return result

print(solution())