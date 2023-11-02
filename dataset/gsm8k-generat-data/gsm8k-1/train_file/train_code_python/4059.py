def solution():
    """There is a square playground that has a side length of 12 meters. There is a maintenance building on the playground that measures 8 meters by 5 meters. How many square meters of the playground is not covered by the maintenance building?"""
    playground_area = 12**2
    building_area = 8 * 5
    remaining_area = playground_area - building_area
    result = remaining_area
    return result

print(solution())