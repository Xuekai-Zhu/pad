def solution():
    """Jason has six fish in his aquarium. He realizes that every day the number of fish doubles. On the third day he takes out one-third of the fish. On the fifth day he takes out one-fourth of the fish. On the seventh day he adds 15 more fish. How many fish in total does he have?"""
    # Define the initial number of fish
    initial_fish = 6

    # Calculate the number of fish each day
    day1_fish = initial_fish
    day2_fish = day1_fish * 2
    day3_fish = day2_fish * 2 - (day2_fish//3)
    day4_fish = day3_fish * 2
    day5_fish = day4_fish * 2 - (day4_fish//4)
    day6_fish = day5_fish * 2
    day7_fish = day6_fish * 2 + 15

    # Calculate the total number of fish
    total_fish = day1_fish + day2_fish + day3_fish + day4_fish + day5_fish + day6_fish + day7_fish

    # Display the total number of fish
    result = total_fish
    return result

print(solution())