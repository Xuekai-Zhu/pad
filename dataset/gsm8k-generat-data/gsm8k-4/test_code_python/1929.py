def solution():
    """Lori owns 15 times as many beanie babies as Sydney. If Lori has 300 beanie babies, how many beanie babies do they have in total?"""
    # Define the number of beanie babies Lori has
    lori_beanies = 300

    # Calculate the number of beanie babies Sydney has
    sydney_beanies = lori_beanies / 15

    # Calculate the total number of beanie babies
    total_beanies = sydney_beanies + lori_beanies

    # return the result
    result = total_beanies
    return result

print(solution())