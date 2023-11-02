def solution():
    # Calculate the number of fish Ryan caught
    ryan = 3 * jason  # Ryan caught three times the number of fish that Jason caught

    # Calculate the total number of fish caught
    total_fish = jason + ryan + jeffery  # Jason, Ryan, and Jeffery caught all the fish

    # Calculate the total number of fish caught, given that Jeffery caught 60 fish
    total_fish = jason + 3 * jason + 60  # Jeffery caught twice the number of fish that Ryan got, and Ryan caught three times the number of fish that Jason caught

    result = total_fish
    return result

print(solution())