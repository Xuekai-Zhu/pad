def solution():
    gnomes_in_westerville = 20
    gnomes_in_ravenswood = gnomes_in_westerville * 4
    percent_taken = 0.4

    # Calculate the number of gnomes taken by the forest owner
    gnomes_taken = gnomes_in_ravenswood * percent_taken

    # Calculate the number of gnomes remaining in Ravenswood forest
    gnomes_remaining = gnomes_in_ravenswood - gnomes_taken
    result = gnomes_remaining
    return result

print(solution())