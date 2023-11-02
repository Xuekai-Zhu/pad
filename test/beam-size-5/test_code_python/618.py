def solution():
    
    # Define the initial number of gum pieces
    initial_gum = 20

    # Calculate the number of gum pieces Jim chews at the school day
    school_gum = initial_gum // 2

    # Calculate the number of gum pieces Jim chews on the way home
    school_gum -= school_gum

    # Calculate the number of gum pieces Jim chews on the way home
    dinner_gum = 2

    # Calculate the number of gum pieces Jim has left after dinner
    remaining_gum = initial_gum - school_gum - dinner_gum

    # Calculate the number of gum pieces Jim gives to his sister
    sister_gum = remaining_gum / 2

    # Calculate the final number of gum pieces Jim has left
    final_gum = remaining_gum - sister_gum

    # Display the final number of gum pieces Jim has left
    result = final_gum
    return

print(solution())