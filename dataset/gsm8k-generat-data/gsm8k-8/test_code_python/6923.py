def solution():
    # Define the dimensions of the garden beds
    length1 = 3
    width1 = 3
    length2 = 4
    width2 = 3

    # Calculate the area of each garden bed
    area1 = length1 * width1
    area2 = length2 * width2

    # Calculate the total growing space
    total_area = 2*area1 + 2*area2

    result = total_area
    return result

print(solution())