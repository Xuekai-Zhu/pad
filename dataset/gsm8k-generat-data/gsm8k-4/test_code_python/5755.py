def solution():
    """John is twice as old as Mary and half as old as Tonya. If Tanya is 60, what is their average age?"""
    
    # Set Tanya's age as 60
    tanya_age = 60
    
    # Calculate John's age
    john_age = tanya_age / 2
    
    # Calculate Mary's age
    mary_age = john_age / 2
    
    # Calculate the average age
    average_age = (john_age + mary_age + tanya_age) / 3
    
    # Return the result
    result = average_age
    return result

print(solution())