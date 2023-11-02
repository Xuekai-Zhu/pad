def solution():
    # Define number of students and their doughnut preferences
    total_students = 25
    num_chocolate = 10
    num_glazed = 15
    
    # Calculate the total cost of chocolate and glazed doughnuts
    cost_chocolate = 2 * num_chocolate
    cost_glazed = 1 * num_glazed
    
    # Calculate the total cost for all doughnuts
    total_cost = cost_chocolate + cost_glazed
    
    result = total_cost
    return result

print(solution())