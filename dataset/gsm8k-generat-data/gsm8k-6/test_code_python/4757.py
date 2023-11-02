def solution():
    # Convert all bags of flour to pounds
    katy_flour = 3 * 5  
    wendi_flour = 2 * katy_flour
    carrie_flour = wendi_flour - 5

    # Convert the flour amounts to ounces
    katy_flour_ounces = katy_flour * 16  
    carrie_flour_ounces = carrie_flour * 16

    # Calculate the difference in flour amounts between Carrie and Katy (in ounces)
    diff_flour = carrie_flour_ounces - katy_flour_ounces
    result = diff_flour
    return result

print(solution())