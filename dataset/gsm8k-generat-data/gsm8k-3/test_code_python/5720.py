def solution():
    """In a building, there are a hundred ladies on the first-floor studying. There are three times that many girls at a party being held on the second floor of the building. How many ladies are on the two floors in total?"""
    # Define the number of ladies on the first floor
    first_floor_ladies = 100

    # Define the number of girls at the party on the second floor
    second_floor_girls = 3 * first_floor_ladies

    # Calculate the total number of ladies on both floors
    total_ladies = first_floor_ladies + second_floor_girls

    # Display the total number of ladies
    result = total_ladies
    return result

print(solution())