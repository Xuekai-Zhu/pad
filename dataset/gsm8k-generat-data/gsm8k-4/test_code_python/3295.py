def solution():
    """Karen and Donald and their 6 children are sharing a beach house with Tom and Eva and their 4 children. If there are 16 legs in the pool, how many people are not in the pool?"""
    # Define the number of people in the pool based on the number of legs
    people_in_pool = 16 // 2  # Each person has 2 legs

    # Define the total number of people staying in the beach house
    total_people = 2 + 6 + 4

    # Calculate the number of people not in the pool
    people_not_in_pool = total_people - people_in_pool

    # return the result
    result = people_not_in_pool
    return result

print(solution())