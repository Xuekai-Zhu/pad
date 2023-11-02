def solution():
    num_parrots_left = 2
    num_crows_left = 1

    # Calculate the original number of parrots
    num_parrots_original = num_parrots_left + num_crows_left

    # Calculate the original number of birds
    num_birds_original = num_parrots_original + num_crows_original

    result = num_birds_original
    return result

print(solution())