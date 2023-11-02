def solution():
    """Johnny is out walking his two dogs at night, and his son joins him for the walk. How many legs' worth of organisms are traveling together for this walk?"""
    # Define the number of legs of each organism
    johnny_legs = 2
    dog_legs = 4
    son_legs = 2

    # Calculate the total number of legs
    total_legs = johnny_legs + (2 * dog_legs) + son_legs

    # return the result
    result = total_legs
    return result

print(solution())