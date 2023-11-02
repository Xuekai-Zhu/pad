def solution():
    # Define the initial number of fish
    num_fish = 6

    # Double the number of fish for each day up to the third day
    for i in range(3):
        num_fish *= 2

    # Take out one-third of the fish on the third day
    num_fish -= num_fish // 3

    # Double the number of fish for each day up to the fifth day
    for i in range(2):
        num_fish *= 2

    # Take out one-fourth of the fish on the fifth day
    num_fish -= num_fish // 4

    # Add 15 fish on the seventh day
    num_fish += 15

    result = num_fish
    return result

print(solution())