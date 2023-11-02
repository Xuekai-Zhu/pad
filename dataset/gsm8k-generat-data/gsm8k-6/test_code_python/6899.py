def solution():
    # Calculate the product of Elvie's age and Arielle's age
    elvie_age = 10
    product = 131 - elvie_age  # since the total sum and product is 131, we subtract Elvie's age to get Arielle's age times Elvie's age
    # Find Arielle's age
    for age in range(1, product + 1):  # loop over all possible ages for Arielle
        if age * elvie_age == product:  # check if the product of their ages is equal to the calculated product
            arielle_age = age
            break
    result = arielle_age
    return result

print(solution())