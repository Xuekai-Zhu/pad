def solution():
    """John has to get a new blanket.  He decides to have a 7 foot by 8-foot quilt made.  The quilt costs $40 per square foot.  How much does his quilt cost?"""
    # Define the dimensions of the quilt in feet
    LENGTH = 7
    WIDTH = 8

    # Calculate the area of the quilt in square feet
    area = LENGTH * WIDTH

    # Calculate the cost of the quilt
    cost = area * 40

    # Display the cost of the quilt
    result = cost
    return result

print(solution())