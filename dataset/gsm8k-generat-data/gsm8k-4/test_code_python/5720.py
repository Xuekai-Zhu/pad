def solution():
    """In a building, there are a hundred ladies on the first-floor studying. There are three times that many girls at a party being held on the second floor of the building. How many ladies are on the two floors in total?"""
    # Define the number of ladies on the first floor
    first_floor_ladies = 100

    # Calculate the number of ladies on the second floor, which is three times the number on the first floor
    second_floor_ladies = first_floor_ladies * 3

    # Calculate the total number of ladies on the two floors
    total_ladies = first_floor_ladies + second_floor_ladies

    # return the result
    result = total_ladies
    return result

print(solution())