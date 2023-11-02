def solution():
    # Define the number of herb plants initially
    basil_bushes = 3
    parsley_plant = 1
    mint_varieties = 2
    total_plants = basil_bushes + parsley_plant + mint_varieties

    # Add the extra basil plant that grew
    total_plants += 1

    # Subtract the mint plants eaten by the rabbit
    total_plants -= 2

    result = total_plants
    return result

print(solution())