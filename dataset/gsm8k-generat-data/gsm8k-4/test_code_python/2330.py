def solution():
    """James paints a 20 ft by 15 ft mural. It takes him 20 minutes to paint 1 square foot and he charges $150 per hour. How much does he charge to paint the mural?"""
    # Define the dimensions of the mural
    width = 20  # feet
    height = 15  # feet

    # Calculate the area of the mural
    area = width * height  # square feet

    # Calculate the time it takes to paint the mural in hours
    time = area * (20 / 60)  # hours

    # Calculate the total cost of painting the mural
    cost = time * 150  # dollars

    # return the result
    result = cost
    return result

print(solution())