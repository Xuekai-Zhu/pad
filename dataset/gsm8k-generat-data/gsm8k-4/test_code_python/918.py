def solution():
    """The house is 20.5 feet by 10 feet. The porch measures 6 feet by 4.5 feet. The house and the porch need shingles. How many square feet of shingles will be needed to roof the house and the porch?"""
    # Define the dimensions of the house and porch
    house_length = 20.5
    house_width = 10
    porch_length = 6
    porch_width = 4.5

    # Calculate the area of the house and porch
    house_area = house_length * house_width
    porch_area = porch_length * porch_width

    # Calculate the total area needing shingles
    total_area = house_area + porch_area

    # return the result
    result = total_area
    return result

print(solution())