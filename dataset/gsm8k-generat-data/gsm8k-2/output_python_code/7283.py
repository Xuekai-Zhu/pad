def solution():
    """Talia is playing football with her friends. The park they're playing at is 5 miles from Talia's house. After their game, Talia is planning to go to the grocery store 3 miles away from the park and 8 miles from her home. Starting and ending at Talia's house, how many miles does Talia drive that day?"""
    park_distance = 5
    grocery_store_distance = 3
    home_grocery_distance = 8
    total_distance = (park_distance * 2) + grocery_store_distance + home_grocery_distance
    result = total_distance
    return result

print(solution())