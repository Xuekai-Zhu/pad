def solution():
    initial_cost_per_person = 0  # Initialize variable for initial cost per person
    final_cost_per_person = 0  # Initialize variable for final cost per person
    
    # Calculate initial cost per person based on 10 friends
    initial_cost_per_person = total_cost / 10
    
    # Calculate final cost per person based on remaining 6 friends
    final_cost_per_person = initial_cost_per_person + 8
    
    # Calculate total cost based on final cost per person and remaining 6 friends
    total_cost = final_cost_per_person * 6
    result = total_cost
    return result

print(solution())