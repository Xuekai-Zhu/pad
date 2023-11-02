def solution():
    # Calculate the number of gnomes in Ravenswood forest
    ravenswood_gnomes = 4 * 20

    # Calculate the number of gnomes taken by the forest owner
    gnomes_taken = 0.4 * ravenswood_gnomes

    # Calculate the number of gnomes remaining in Ravenswood forest
    gnomes_remaining = ravenswood_gnomes - gnomes_taken
    result = gnomes_remaining
    return result

print(solution())