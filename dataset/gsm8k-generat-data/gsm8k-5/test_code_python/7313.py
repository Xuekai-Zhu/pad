def solution():
    hats_per_yard = 4  # James can make 4 hats out of one yard of velvet
    velvet_per_cloak = 3  # James needs 3 yards of velvet to make one cloak
    num_cloaks = 6  # James wants to make 6 cloaks
    num_hats = 12  # James wants to make 12 hats

    # Calculate the total amount of velvet needed for the cloaks
    velvet_for_cloaks = velvet_per_cloak * num_cloaks

    # Calculate the total number of yards of velvet needed for the hats
    total_hats = num_hats * hats_per_yard
    velvet_for_hats = total_hats / 3

    # Calculate the total amount of velvet needed
    total_velvet = velvet_for_cloaks + velvet_for_hats
    result = total_velvet
    return result

print(solution())