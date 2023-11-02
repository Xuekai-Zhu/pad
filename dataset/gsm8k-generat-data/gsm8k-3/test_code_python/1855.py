def solution():
    """In a town where 60% of the citizens own a pet, half own a dog and 30 own a cat. How many citizens are in the town?"""
    # Calculate the percentage of citizens who own a dog
    dog_percentage = 0.5 * 60  # 30% own a cat, so 60-30=30% own a dog

    # Calculate the total number of pet owners
    pet_owners = (dog_percentage + 30) / 60  # Convert to decimal and find total percentage

    # Calculate the total number of citizens
    total_citizens = int(round(pet_owners / 0.6))  # Convert back to integer and round

    # Display the total number of citizens
    result = total_citizens
    return result

print(solution())