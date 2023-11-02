def solution():
    # Define the original number of parrots as p and the original number of crows as c
    # We also know that p + c = the original number of birds
    # After the noise, p-2 parrots and c-2 crows are left on the branch
    # We know that p-2 = 2 and c-2 = 1, so we can solve for p and c
    p = 4
    c = 3

    # Calculate the original number of birds
    original_num_birds = p + c
    result = original_num_birds
    return result

print(solution())