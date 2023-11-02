def solution():
    """Talia is playing football with her friends. The park they're playing at is 5 miles from Talia's house. After their game, Talia is planning to go to the grocery store 3 miles away from the park and 8 miles from her home. Starting and ending at Talia's house, how many miles does Talia drive that day?"""
    # Define the distance from the park to Talia's house
    park_distance = 5

    # Define the distance from the grocery store to Talia's house
    grocery_distance = 8

    # Define the distance from the grocery store to the park
    grocery_park_distance = 3

    # Calculate the total distance Talia drives that day
    total_distance = park_distance + grocery_park_distance + grocery_distance

    # Return the result
    result = total_distance
    return result

print(solution())