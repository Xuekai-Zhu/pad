def solution():
    """Haley is making cider. It takes 20 golden delicious apples and 40 pink lady apples to make one pint of cider. Each of her 6 farmhands can pick 240 apples per hour and will work 5 hours today. How many pints of cider can Haley make with the apples gathered today, provided that the ratio of golden delicious apples to pink lady apples gathered is 1:2?"""
    # Define the number of apples needed to make one pint of cider
    apples_per_pint = 20 + 40 * 2

    # Calculate the total number of apples gathered
    total_apples = 6 * 240 * 5

    # Calculate the number of pints of cider that can be made
    pints_of_cider = total_apples // apples_per_pint

    result = pints_of_cider
    return result

print(solution())