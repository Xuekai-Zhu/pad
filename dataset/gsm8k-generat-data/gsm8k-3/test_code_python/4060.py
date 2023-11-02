def solution():
    """There is a square playground that has a side length of 12 meters. There is a maintenance building on the playground that measures 8 meters by 5 meters. How many square meters of the playground is not covered by the maintenance building?"""
    # Define the length of the side of the square playground
    playground_side = 12

    # Define the length and width of the maintenance building
    building_length = 8
    building_width = 5

    # Calculate the area of the maintenance building
    building_area = building_length * building_width

    # Calculate the area of the square playground
    playground_area = playground_side ** 2

    # Calculate the area of the playground not covered by the maintenance building
    uncovered_area = playground_area - building_area

    # Display the uncovered area
    result = uncovered_area
    return result

print(solution())