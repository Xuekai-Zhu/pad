def solution():
    """Paddy's Confidential has 600 cans of stew required to feed 40 people. How many cans would be needed to feed 30% fewer people?"""
    # Define the initial number of cans and people
    initial_cans = 600
    initial_people = 40
    
    # Calculate the number of cans needed per person
    cans_per_person = initial_cans / initial_people
    
    # Calculate the new number of people after a 30% decrease
    new_people = initial_people * 0.7
    
    # Calculate the new number of cans needed
    new_cans = cans_per_person * new_people
    
    # Return the result
    result = new_cans
    return result

print(solution())