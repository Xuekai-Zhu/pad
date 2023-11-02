def solution():
    
    ham_sandwiches = 10
    cheese_per_ham_sandwich = 2
    cheese_per_grilled_cheese = 3
    total_cheese_used = 50
    cheese_used_in_ham_sandwiches = ham_sandwiches * cheese_per_ham_sandwich
    cheese_used_in_grilled_cheese = total_cheese_used - cheese_used_in_ham_sandwiches
    grilled_cheese_sandwiches = cheese_used_in_grilled_cheese / cheese_per_grilled_cheese
    result = grilled_cheese_sandwiches
    return result

print(solution())