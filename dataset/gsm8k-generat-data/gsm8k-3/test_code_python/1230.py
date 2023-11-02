def solution():
    """Casey wants to decorate her toenails and fingernails. First, she wants to do a base coat on each nail, then a coat of paint and finally a coat of glitter on every nail. It takes 20 minutes to apply each coat and 20 minutes for each coat to dry before applying the next one. Assuming Casey's nails will be done when all coats have been applied and dried, how many minutes will it take her to finish decorating her fingernails and toenails?"""
    # Define the time it takes to apply and dry each coat
    COAT_TIME = 20

    # Calculate the time it takes to do one set of nails
    nail_time = COAT_TIME * 3 + COAT_TIME * 3

    # Calculate the time it takes to do all of Casey's nails
    total_nail_time = nail_time * 20

    # Display the total time
    result = total_nail_time
    return result

print(solution())