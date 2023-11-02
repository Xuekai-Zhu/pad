def solution():
    """Kendra wants enough shirts that she only has to do laundry once every two weeks.
    She wears one shirt to school for each of the five weekdays.
    Three days a week, she changes into a different shirt for an after-school club.
    On Saturday, she wears one shirt all day.
    On Sunday, she wears a different shirt to church than she does for the rest of the day.
    How many shirts does she need to be able to only do laundry once every two weeks?"""
    
    # Calculate the total number of shirts Kendra wears in a week
    daily_shirts = 5 + 3 + 1 + 2 # weekday shirts + after-school club shirts + Saturday shirt + Sunday shirts
    
    # Calculate the total number of shirts Kendra wears in two weeks
    biweekly_shirts = 2 * daily_shirts
    
    # Return the result
    result = biweekly_shirts
    return result

print(solution())