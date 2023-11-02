def solution():
    
    total_cost = 800
    sale_puppy_cost = 150
    num_sale_puppies = 3
    num_other_puppies = 2
    cost_of_other_puppies = (total_cost - (sale_puppy_cost * num_sale_puppies)) / num_other_puppies
    result = cost_of_other_puppies
    return result

print(solution())