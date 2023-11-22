def solution():
    
    # Define the total number of shells
    total_shells = 700

    # Calculate the number of shells found by Team Alphas
    alphas_shells = total_shells * 0.4

    # Calculate the number of shells remaining after Team Alphas found their share
    remaining_shells = total_shells - alphas_shells

    # Calculate the number of shells found by Team The finders
    finders_shells = remaining_shells * 0.6

    # Calculate the number of shells found by Team Gogetters
    gogetters_shells = total_shells - alphas_shells - finders_shells

    # Display the number of shells found by Team Gogetters
    result = gogetters_shells
    return result

print(solution())