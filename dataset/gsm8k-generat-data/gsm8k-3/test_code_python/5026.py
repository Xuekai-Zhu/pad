def solution():
    """If Aang caught 7 fish, then Sokka caught 5 fish, and then Toph caught 12 fish, what is the average amount of fish that each person caught?"""
    # Define the number of fish caught by each person
    aang_fish = 7
    sokka_fish = 5
    toph_fish = 12

    # Calculate the total number of fish caught
    total_fish = aang_fish + sokka_fish + toph_fish

    # Calculate the average number of fish caught per person
    average_fish = total_fish / 3

    # Display the average number of fish caught
    result = average_fish
    return result

print(solution())