def solution():
    """Donna is catering for a party. She makes 20 sandwiches and then cuts them in half, before cutting them in half again. She then gives everyone 8 portions. How many people can she feed?"""
    # Define the initial number of sandwiches
    sandwiches = 20

    # Cut the sandwiches in half twice
    portions = sandwiches * 2 * 2

    # Calculate the number of people that can be fed
    num_people = portions // 8

    # Return the result
    result = num_people 
    return result

print(solution())