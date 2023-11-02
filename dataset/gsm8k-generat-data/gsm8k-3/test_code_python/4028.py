def solution():
    """Lucas wants to get a dog but his parents think he already has too many pets and won't have enough space. He already has 12 pet beds in his room but manages to fit another 8 pet beds. His parents argue that each pet is going to need 2 beds each to feel comfortable. According to his parent's argument, how many pets does Lucas have enough room for?"""
    # Define the number of pet beds Lucas has available
    available_beds = 12 + 8

    # Define the number of beds each pet needs
    beds_per_pet = 2

    # Calculate the maximum number of pets Lucas can have
    max_pets = available_beds // beds_per_pet

    # Display the maximum number of pets Lucas can have
    result = max_pets
    return result

print(solution())