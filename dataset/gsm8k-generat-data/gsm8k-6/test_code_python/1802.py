def solution():
    # Calculate the final number of fish after all the operations
    num_fish = 6 * (2**7)  # number of fish doubles every day for 7 days
    num_fish -= num_fish / 3  # on third day, he takes out one-third of the fish
    num_fish -= num_fish / 4  # on fifth day, he takes out one-fourth of the fish
    num_fish += 15  # on seventh day, he adds 15 more fish
    result = num_fish
    return result

print(solution())