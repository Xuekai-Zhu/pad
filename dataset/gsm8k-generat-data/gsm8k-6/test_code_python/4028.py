def solution():
    # Calculate the number of pets Lucas can have based on the number of pet beds he has
    available_beds = 12 + 8  # Lucas has 12 pet beds and manages to fit another 8
    max_pets = available_beds // 2  # each pet needs 2 beds, so max number of pets that can fit is half of the total number of beds
    result = max_pets
    return result

print(solution())