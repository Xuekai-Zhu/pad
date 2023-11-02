def solution():
    """Thomas is 6 years old. His older sister, Shay, is 13 years older than him and 5 years younger than their older brother, James. How old will James be by the time Thomas reaches his current age?"""
    # Define Thomas' age
    thomas_age = 6
    
    # Calculate Shay's age
    shay_age = thomas_age + 13
    
    # Calculate James' age
    james_age = shay_age + 5
    
    # Calculate the age difference between James and Thomas
    age_difference = james_age - thomas_age
    
    # Calculate James' age when Thomas reaches his current age
    james_age_when_thomas_reaches_current_age = james_age + age_difference
    
    result = james_age_when_thomas_reaches_current_age
    return result

print(solution())