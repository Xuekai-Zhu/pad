def solution():
    """John has to get a new blanket. He decides to have a 7 foot by 8-foot quilt made. The quilt costs $40 per square foot. How much does his quilt cost?"""
    # Define the dimensions of the quilt
    length = 7
    width = 8

    # Calculate the area of the quilt
    area = length * width

    # Calculate the cost of the quilt
    cost = area * 40

    # Return the cost
    result = cost
    return result

print(solution())