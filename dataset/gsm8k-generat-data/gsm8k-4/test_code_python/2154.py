def solution():
    """The spacecraft Gibraltar is a mountain-sized intergalactic vehicle for transporting equipment, building materials, and families to establish colonies on far-away planets.  At full capacity, the vehicle can carry 300 family units with four people per family.  The space flight is expected to take years, and it is expected that the size of families will grow during the space voyage.  Therefore, when the spacecraft leaves the earth, it will carry 100 people less than one-third of the ship's capacity.  How many people will be on the ship to start the journey?"""
    # Define the maximum number of family units the ship can carry
    max_families = 300

    # Calculate the maximum number of people the ship can carry
    max_people = max_families * 4

    # Calculate the number of people on the ship when it leaves the earth
    start_people = (max_people / 3) - 100

    result = start_people
    return result

print(solution())