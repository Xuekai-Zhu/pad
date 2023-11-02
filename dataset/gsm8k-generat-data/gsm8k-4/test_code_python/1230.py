def solution():
    """Casey wants to decorate her toenails and fingernails. First, she wants to do a base coat on each nail, then a coat of paint and finally a coat of glitter on every nail. It takes 20 minutes to apply each coat and 20 minutes for each coat to dry before applying the next one. Assuming Casey's nails will be done when all coats have been applied and dried, how many minutes will it take her to finish decorating her fingernails and toenails?"""
    # Define the number of nails to be decorated
    num_nails = 20

    # Define the time it takes to apply and dry each coat
    coat_time = 20

    # Calculate the total time to apply and dry all coats
    total_time = (3 * num_nails * coat_time)

    # Return the result
    result = total_time
    return result

print(solution())