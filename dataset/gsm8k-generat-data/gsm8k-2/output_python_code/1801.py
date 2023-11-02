def solution():
    """Jason has six fish in his aquarium. He realizes that every day the number of fish doubles. On the third day he takes out one-third of the fish. On the fifth day he takes out one-fourth of the fish. On the seventh day he adds 15 more fish. How many fish in total does he have?"""
    num_fish = 6
    for i in range(1, 8):
        num_fish *= 2
        if i == 3:
            num_fish = int(num_fish * (2/3))
        elif i == 5:
            num_fish = int(num_fish * (3/4))
        elif i == 7:
            num_fish += 15
    result = num_fish
    return result

print(solution())