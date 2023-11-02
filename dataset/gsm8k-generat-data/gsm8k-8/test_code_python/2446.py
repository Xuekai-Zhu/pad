def solution():
    # Define the number of skips Bob and Jim can do per rock
    bob_skips_per_rock = 12
    jim_skips_per_rock = 15

    # Define the number of rocks they each skipped
    bob_rocks_skipped = 10
    jim_rocks_skipped = 10

    # Calculate the total number of skips
    total_skips = bob_skips_per_rock * bob_rocks_skipped + jim_skips_per_rock * jim_rocks_skipped
    result = total_skips
    return result

print(solution())