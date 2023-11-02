def solution():
    """James makes potatoes for a group.  Each person eats 1.5 pounds of potatoes.  He makes potatoes for 40 people.  A 20-pound bag of potatoes costs $5.  How much does it cost?"""
    
    # Define the amount of potatoes needed for one person and the number of people
    potatoes_per_person = 1.5
    num_people = 40
    
    # Calculate the total amount of potatoes needed
    total_potatoes = potatoes_per_person * num_people
    
    # Calculate the number of bags of potatoes needed
    bags_needed = total_potatoes / 20
    
    # Calculate the total cost of the potatoes
    total_cost = bags_needed * 5
    
    # Display the total cost
    result = total_cost
    return result

print(solution())