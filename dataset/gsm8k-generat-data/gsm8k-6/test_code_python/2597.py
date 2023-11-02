def solution():
    # Calculate the number of rehabilitation centers visited by Jude
    jude_centers = (1/2) * 6  # Jude visited half the number of centers Lisa did

    # Calculate the number of rehabilitation centers visited by Han
    han_centers = (2 * jude_centers) - 2  # Han visited 2 less than twice the number of centers Jude did

    # Calculate the number of rehabilitation centers visited by Jane
    jane_centers = (2 * han_centers) + 6  # Jane visited 6 more than twice the number of centers Han did

    # Calculate the total number of rehabilitation centers visited by all of them
    total_centers = lisa_centers + jude_centers + han_centers + jane_centers

    result = total_centers
    return result

print(solution())