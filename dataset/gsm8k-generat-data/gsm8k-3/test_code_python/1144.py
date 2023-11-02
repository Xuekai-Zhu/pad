def solution():
    """Michael has two brothers. His oldest brother is 1 year older than twice Michael's age when Michael was a year younger.
    His younger brother is 5 years old, which is a third of the age of the older brother. What is their combined age?"""
    
    # Calculate Michael's age
    michael_age = 3 * 5  # Michael's younger brother is a third of the age of the older brother, who is 15 years old
    michael_age -= 1  # Michael was a year younger
    
    # Calculate the oldest brother's age
    oldest_brother_age = 2 * michael_age + 1
    
    # Calculate the combined age of all three brothers
    total_age = michael_age + oldest_brother_age + 5
    
    result = total_age
    return result

print(solution())