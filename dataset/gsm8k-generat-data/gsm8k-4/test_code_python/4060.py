def solution():
    """There is a square playground that has a side length of 12 meters. There is a maintenance building on the playground that measures 8 meters by 5 meters. How many square meters of the playground is not covered by the maintenance building?"""
    # Define the side length of the square playground
    playground_side = 12

    # Define the dimensions of the maintenance building
    maintenance_building_length = 8
    maintenance_building_width = 5

    # Calculate the area of the maintenance building
    maintenance_building_area = maintenance_building_length * maintenance_building_width

    # Calculate the area of the square playground
    playground_area = playground_side ** 2

    # Calculate the area not covered by the maintenance building
    uncovered_area = playground_area - maintenance_building_area

    # return the result
    result = uncovered_area
    return result

print(solution())