def solution():
    """Jillian, Savannah, and Clayton were collecting shells on the beach. Jillian collected 29,
    Savannah collected 17, and Clayton collected 8. They decided that they wanted to give the shells to two of their friends
    who had just arrived. They put their shells together and distributed them evenly to each friend.
    How many shells did each friend get?"""
    # Define the number of shells collected by each person
    jillian_shells = 29
    savannah_shells = 17
    clayton_shells = 8

    # Calculate the total number of shells collected
    total_shells = jillian_shells + savannah_shells + clayton_shells

    # Calculate the number of shells each friend should get
    friend_shells = total_shells / 2

    # Return the result
    result = friend_shells
    return result

print(solution())