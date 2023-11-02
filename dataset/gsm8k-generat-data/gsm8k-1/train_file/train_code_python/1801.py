def solution():
    """Jason has six fish in his aquarium. He realizes that every day the number of fish doubles. On the third day he takes out one-third of the fish. On the fifth day he takes out one-fourth of the fish. On the seventh day he adds 15 more fish. How many fish in total does he have?"""
    num_fish = 6
    num_fish *= 2**2  # after doubling for 3 days
    num_fish -= num_fish // 3  # removing one-third on third day
    num_fish *= 2**2  # doubling for next 2 days
    num_fish -= num_fish // 4  # removing one-fourth on fifth day
    num_fish *= 2**2  # doubling for next 2 days
    num_fish += 15  # adding 15 on seventh day
    result = num_fish
    return result

print(solution())