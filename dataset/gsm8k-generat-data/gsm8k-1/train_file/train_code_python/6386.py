def solution():
    """A 10 m long and 8 m wide rectangular floor is to be covered with a square carpet with 4 m sides. How many square meters of the floor are uncovered?"""
    floor_area = 10 * 8
    carpet_area = 4 * 4
    uncovered_area = floor_area % carpet_area
    result = uncovered_area
    return result

print(solution())