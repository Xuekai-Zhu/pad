def solution():
    # Calculate the total number of pieces of popcorn that Jared's friends can eat
    total_friends_popcorn = 60 * 3

    # Calculate the total number of pieces of popcorn that all four of them can eat
    total_popcorn = total_friends_popcorn + 90

    # Calculate the number of servings needed
    servings_needed = total_popcorn / 30

    result = servings_needed
    return result

print(solution())