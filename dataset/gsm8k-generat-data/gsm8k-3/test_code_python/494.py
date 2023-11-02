def solution():
    """There is a 5,200 sq. ft. house and a 7,300 sq. ft. house next to each other. The smaller house is being expanded. If the new total square footage of both houses is 16,000 sq. ft., how much is the smaller house being expanded by, in sq. ft.?"""
    # Define the original square footage of the houses
    house1_sqft = 5200
    house2_sqft = 7300

    # Calculate the total square footage of both houses
    total_sqft = 16000

    # Calculate the new square footage of the smaller house
    new_house1_sqft = (total_sqft - house2_sqft)

    # Calculate how much the smaller house is being expanded by
    expansion = new_house1_sqft - house1_sqft

    # Display the expansion amount
    result = expansion
    return result

print(solution())