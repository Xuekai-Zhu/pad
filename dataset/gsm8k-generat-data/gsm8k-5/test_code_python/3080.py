def solution():
    starting_fish = 2  # Tony starts with 2 fish
    fish_per_year = 2  # Tony's parents buy him 2 fish every year
    years = 5  # Tony wants to know how many fish he will have in 5 years

    # Calculate the number of fish Tony will have in 5 years
    total_fish = starting_fish + ((fish_per_year - 1) * years)

    result = total_fish
    return result

print(solution())