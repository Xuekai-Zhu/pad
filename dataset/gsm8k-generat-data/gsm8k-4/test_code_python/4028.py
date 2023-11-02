def solution():
    """Lucas wants to get a dog but his parents think he already has too many pets and won't have enough space. He already has 12 pet beds in his room but manages to fit another 8 pet beds. His parents argue that each pet is going to need 2 beds each to feel comfortable. According to his parent's argument, how many pets does Lucas have enough room for?"""
    # Define the number of pet beds available and the number of additional pet beds
    initial_bed_count = 12
    additional_bed_count = 8

    # Calculate the total number of pet beds
    total_bed_count = initial_bed_count + additional_bed_count

    # Define the number of pet beds required per pet
    beds_per_pet = 2

    # Calculate the maximum number of pets Lucas can have based on the available beds
    max_pets = total_bed_count // beds_per_pet

    result = max_pets
    return result

print(solution())