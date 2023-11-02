def solution():
    """There is a 5,200 sq. ft. house and a 7,300 sq. ft. house next to each other. The smaller house is being expanded. If the new total square footage of both houses is 16,000 sq. ft., how much is the smaller house being expanded by, in sq. ft.?"""
    # Define the initial sizes of the two houses
    smaller_house = 5200
    larger_house = 7300

    # Calculate the total size of both houses
    total_size = smaller_house + larger_house

    # Calculate the size of the expansion
    expansion = 16000 - total_size

    # return the result
    result = expansion
    return result

print(solution())