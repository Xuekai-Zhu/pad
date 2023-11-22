def solution():
    
    # Define the number of new potted plants
    new_plants = 18

    # Define the number of window ledges
    num_ledges = 40

    # Calculate the total number of potted plants
    total_plants = new_plants + 2*num_ledges

    # Calculate the number of plants given to friends and family tomorrow
    plants_given = num_ledges * 1

    # Calculate the number of plants remaining with Mary
    plants_remaining = total_plants - plants_given

    # Display the number of plants remaining with Mary
    result = plants_remaining
    return result

print(solution())