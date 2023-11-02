def solution():
    """Matt's entire family was going to spend the week at the lake house for vacation. Matt's family included his mom, dad, his older brother and his wife and their 4 kids. His Uncle Joe and his wife were also coming and would bring their 3 kids. The house only sleeps 4 people. Everyone else would sleep 2 to a tent outside. How many tents would they need?"""
    # Count the number of people in the family, including Matt
    num_people = 1 + 2 + 1 + 1 + 4 + 2 + 2 + 3
    
    # Calculate the number of people that can sleep in the house
    house_capacity = 4
    
    # Calculate the number of people that cannot sleep in the house
    tent_capacity = num_people - house_capacity
    
    # Calculate the number of tents needed
    num_tents = tent_capacity / 2
    
    # Round up to the nearest integer
    num_tents = int(num_tents + 0.5)
    
    # Return the result
    return num_tents

print(solution())