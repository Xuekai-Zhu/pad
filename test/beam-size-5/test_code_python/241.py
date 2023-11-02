def solution():
    
    # Define the number of snails in the first aquarium and the number of snails in the second aquarium
    first_aquarium_snails = 4
    second_aquarium_snails = 32

    # Calculate the number of snails in the two aquariums
    two_aquarium_snails = 2 * first_aquarium_snails

    # Calculate the total number of snails in both aquariums
    total_both_aquariums = first_aquarium_snails + second_aquarium_snails

    # Calculate the number of fish in each aquarium
    fish_per_aquarium = total_both_aquariums / 2

    # Display the number of fish in each aquarium
    result = fish_per_aquarium
    return result

print(solution())