def solution():
    
    ham_cheese_slices = 2
    grilled_cheese_slices = 3
    total_cheese_slices = 50
    ham_sandwiches = 10
    ham_cheese_used = ham_sandwiches * ham_cheese_slices
    grilled_cheese_used = total_cheese_slices - ham_cheese_used
    grilled_cheese_sandwiches = grilled_cheese_used // grilled_cheese_slices
    result = grilled_cheese_sandwiches
    return result

print(solution())