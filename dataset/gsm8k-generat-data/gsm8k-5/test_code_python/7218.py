def solution():
    starting_gum = 10  # Adrianna starts with 10 pieces of gum
    extra_gum = 3  # Adrianna buys 3 more pieces of gum at the store
    friends = 11  # Adrianna gives gum to 11 friends

    # Calculate how many pieces of gum Adrianna has left after giving some away
    remaining_gum = starting_gum + extra_gum - friends
    result = remaining_gum
    return result

print(solution())