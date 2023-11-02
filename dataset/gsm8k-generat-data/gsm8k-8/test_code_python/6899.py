def solution():
    # Define Elvie's age
    elvie_age = 10
    
    # Calculate the sum of Elvie's age and Arielle's age
    sum_age = 131 - elvie_age
    
    # Find the possible factors of the product of Elvie's age and Arielle's age
    product_age = elvie_age * arielle_age
    
    possible_factors = []
    for i in range(1, product_age + 1):
        if product_age % i == 0:
            possible_factors.append(i)
    
    # Iterate through the possible factors and check which one adds up to the sum of their ages
    for factor in possible_factors:
        if factor + elvie_age == sum_age:
            arielle_age = factor
            break
    
    result = arielle_age
    return result

print(solution())