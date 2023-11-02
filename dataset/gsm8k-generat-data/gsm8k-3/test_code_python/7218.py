def solution():
    """Adrianna has 10 pieces of gum to share with her friends. There wasn't enough gum for all her friends, so she went to the store to get 3 more pieces of gum. She gave out gum to 11 friends. How many pieces of gum does Adrianna have now?"""
    # Define the initial number of gum pieces and the number of friends
    INITIAL_GUM = 10
    NUM_FRIENDS = 11

    # Calculate the total number of gum pieces after Adrianna goes to the store
    total_gum = INITIAL_GUM + 3

    # Calculate the number of gum pieces Adrianna has left after giving some to her friends
    remaining_gum = total_gum - NUM_FRIENDS

    # Display the remaining number of gum pieces
    result = remaining_gum
    return result

print(solution())