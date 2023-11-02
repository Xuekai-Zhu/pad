def solution():
    """How many legs does a spider have if it has two times more than double the number of legs a human has?"""
    
    # Define the number of legs a human has
    human_legs = 2 * 2  # Two legs per human, multiplied by 2 to get the double

    # Calculate the number of legs a spider has
    spider_legs = 2 * human_legs + 2  # Two times more than double, plus 2 for the extra pair

    # Return the number of legs a spider has
    result = spider_legs
    return result

print(solution())