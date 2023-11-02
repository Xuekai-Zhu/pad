def solution():
    """Adrianna has 10 pieces of gum to share with her friends. There wasn't enough gum for all her friends, so she went to the store to get 3 more pieces of gum. She gave out gum to 11 friends. How many pieces of gum does Adrianna have now?"""
    # Define the initial number of gum pieces and the number of friends
    initial_gum = 10
    num_friends = 11

    # Check if there is enough gum for all the friends
    if initial_gum < num_friends:
        # If not, buy more gum
        additional_gum = 3
        total_gum = initial_gum + additional_gum
    else:
        # If yes, keep the initial number of gum pieces
        total_gum = initial_gum

    # Subtract the number of gum pieces given to friends
    remaining_gum = total_gum - num_friends

    # Return the result
    result = remaining_gum
    return result

print(solution())