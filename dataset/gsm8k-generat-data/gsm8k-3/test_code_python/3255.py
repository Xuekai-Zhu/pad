def solution():
    """April went to a concert that has two bands. 2/3 of the audience was there for
    the second band and 1/3 was there for the first band. 50% of the audience there for
    the second band is under the age of 30. Of this group, 60% are women and there
    are 20 men. How many people are at the concert?"""
    
    # Calculate the number of people at the concert
    # Let x be the total number of people at the concert
    # Then (2/3)x is the number of people at the second band
    # and (1/3)x is the number of people at the first band
    # Let y be the number of people under 30 at the second band
    # Then (1/2)(2/3)x = (1/3)x is the number of people over 30 at the second band
    # Let z be the number of women under 30 at the second band
    # Then 0.6y = 20 is the number of men under 30 at the second band
    
    x = (20 * 10 / 3) / 0.6
    # Simplifying, we get x = 111.11
    
    # Round up to the nearest whole number
    total_people = round(x)
    
    # Display the total number of people
    result = total_people
    return result

print(solution())