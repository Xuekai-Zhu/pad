def solution():
    """There are 30 pieces of popcorn in a serving. Jared can eat 90 pieces of popcorn and his three other friends can each eat 60 pieces of popcorn. How many servings of popcorn should Jared order for all of them?"""
    # Define the number of pieces of popcorn in a serving
    POPCORN_PER_SERVING = 30

    # Define the number of pieces of popcorn each person can eat
    jared_popcorn = 90
    friend_popcorn = 60

    # Calculate the total number of pieces of popcorn
    total_popcorn = jared_popcorn + (3 * friend_popcorn)

    # Calculate the number of servings needed
    servings_needed = total_popcorn // POPCORN_PER_SERVING
    if total_popcorn % POPCORN_PER_SERVING != 0:
        servings_needed += 1

    # Display the number of servings needed
    result = servings_needed
    return result

print(solution())