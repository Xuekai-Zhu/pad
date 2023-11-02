def solution():
    cups_sold_to_construction_crew = 0.5 * cups_made  # Half of the lemonade was sold to the construction crew
    cups_sold_to_kids_on_bikes = 18  # Hazel sold 18 cups to kids on bikes
    cups_given_to_friends = 0.5 * cups_sold_to_kids_on_bikes  # Half of the cups sold to kids on bikes were given away to friends
    cups_drunk_by_hazel = 1  # Hazel drank the last cup herself

    # Calculate the number of cups Hazel made
    total_cups = cups_sold_to_construction_crew + cups_sold_to_kids_on_bikes + cups_given_to_friends + cups_drunk_by_hazel
    result = total_cups
    return result

print(solution())