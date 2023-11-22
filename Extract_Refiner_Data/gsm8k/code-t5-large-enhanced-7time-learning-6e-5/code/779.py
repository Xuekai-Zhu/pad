def solution():
    
    # Define the initial number of orange and white fish
    orange_fish = 3
    white_fish = 4

    # Subtract the sales assistant from the total number of fish
    total_fish = orange_fish + white_fish - 17

    # Calculate the new number of orange fish after adding the sales assistant
    new_orange_fish = 2 * white_fish

    # Add the sales assistant to the total number of fish
    total_fish += 17

    # Calculate the new number of white fish
    new_white_fish = total_fish - new_orange_fish

    # Display the new number of white fish
    result = new_white_fish
    return result

print(solution())