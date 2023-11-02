def solution():
    """Melany has to fence a 5000 feet square field with wire mesh. If one foot of wire mesh is sold at $30, and she had $120000, how many feet of the field will not be fenced?"""
    # Define the cost per foot of wire mesh
    COST_PER_FOOT = 30

    # Define the total amount of money Melany has to spend on wire mesh
    TOTAL_COST = 120000

    # Calculate the total number of feet of wire mesh Melany can buy
    total_feet = TOTAL_COST / COST_PER_FOOT

    # Calculate the length of each side of the square field
    side_length = round((total_feet / 4) ** 0.5)

    # Calculate the total area of the square field
    total_area = side_length ** 2

    # Calculate the number of feet that will not be fenced
    un-fenced_feet = 5000 - total_area

    # Display the number of feet that will not be fenced
    result = unfenced_feet
    return result

print(solution())