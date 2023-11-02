def solution():
    """Dabbie bought 3 turkeys for thanksgiving, the first turkey is 6 kilograms, the second turkey is 9 kilograms, and the weight of the third turkey is twice the weight
    of the second turkey. If the cost of a kilogram of turkey is $2, how much does Dabbie spent on all the turkeys?"""
    
    # Define the weights of the turkeys
    turkey1 = 6
    turkey2 = 9
    turkey3 = turkey2 * 2
    
    # Calculate the total weight of the turkeys
    total_weight = turkey1 + turkey2 + turkey3
    
    # Calculate the total cost of the turkeys
    cost_per_kilo = 2
    total_cost = total_weight * cost_per_kilo
    
    # Display the total cost
    result = total_cost
    return result

print(solution())