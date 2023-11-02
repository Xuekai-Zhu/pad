def solution():
    """There were 50 people on the city bus. At the first stop, 15 people got off. At the next stop 8 people got off and 2 got on. At the third stop, 4 people got off and 3 people got on. How many people are on the bus after the third stop?"""
    # Define the initial number of people on the bus
    num_people = 50

    # Subtract the number of people who got off and add the number who got on at the first stop
    num_people -= 15

    # Subtract the number of people who got off and add the number who got on at the second stop
    num_people -= 8
    num_people += 2

    # Subtract the number of people who got off and add the number who got on at the third stop
    num_people -= 4
    num_people += 3

    # return the result
    result = num_people
    return result

print(solution())