def solution():
    num_orchids = 5
    num_daisies = 4
    num_orchids_petals = 5
    num_daisies_petals = 10

    # Calculate the total number of petals of the orchids
    total_orchid_petals = num_orchids * num_orchids_petals

    # Calculate the total number of petals of the daisies
    total_daisie_petals = num_daisies * num_daisies_petals

    # Calculate the difference in petals between the daisies and the orchids
    diff_petals = total_daisie_petals - total_orchid_petals
    result = diff_petals
    return result

print(solution())