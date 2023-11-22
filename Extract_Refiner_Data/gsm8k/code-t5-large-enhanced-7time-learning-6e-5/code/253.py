def solution():
    
    # Define the height of the redwood in feet
    height = 200

    # Calculate the weight of each section of the redwood tree
    section_weight = 400 / 10

    # Calculate the weight of the termsites
    termites_weight = section_weight * 0.3

    # Calculate the total weight of the redwood tree
    total_weight = height * section_weight + termites_weight

    # Display the total weight of the redwood tree
    result = total_weight
    return result

print(solution())