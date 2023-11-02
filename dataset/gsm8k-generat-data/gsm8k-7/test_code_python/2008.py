def solution():
    percent_with_pearls = 0.25
    num_oysters_per_dive = 16
    num_pearls_needed = 56

    # Calculate the number of oysters with pearls per dive
    num_with_pearls_per_dive = percent_with_pearls * num_oysters_per_dive

    # Calculate the number of dives needed to collect the desired number of pearls
    num_dives_needed = num_pearls_needed / num_with_pearls_per_dive
    result = num_dives_needed
    return result

print(solution())