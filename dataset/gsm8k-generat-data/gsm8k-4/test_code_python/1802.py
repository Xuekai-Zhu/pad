def solution():
    """Jason has six fish in his aquarium. He realizes that every day the number of fish doubles. On the third day he takes out one-third of the fish. On the fifth day he takes out one-fourth of the fish. On the seventh day he adds 15 more fish. How many fish in total does he have?"""
    # Define the initial number of fish
    fish = 6

    # Calculate the number of fish on the third day after taking out one-third
    fish_third_day = int(fish * 2 ** 3 * (2/3))

    # Calculate the number of fish on the fifth day after taking out one-fourth
    fish_fifth_day = int(fish_third_day * 2 ** 2 * (3/4))

    # Calculate the number of fish on the seventh day after adding 15 fish
    fish_seventh_day = fish_fifth_day * 2 ** 2 + 15

    # Calculate the total number of fish
    total_fish = fish + fish_third_day + fish_fifth_day + fish_seventh_day

    # Return the result
    result = total_fish
    return result

print(solution())