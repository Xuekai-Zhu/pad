def solution():
    num_lori_beanies = 300
    lori_multiple = 15

    # Calculate Sydney's number of beanie babies
    num_sydney_beanies = num_lori_beanies / lori_multiple

    # Calculate the total number of beanie babies
    total_beanies = num_lori_beanies + num_sydney_beanies
    result = total_beanies
    return result

print(solution())