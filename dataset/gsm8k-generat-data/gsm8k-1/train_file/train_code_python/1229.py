def solution():
    """Casey wants to decorate her toenails and fingernails. First, she wants to do a base coat on each nail, then a coat of paint and finally a coat of glitter on every nail. It takes 20 minutes to apply each coat and 20 minutes for each coat to dry before applying the next one. Assuming Casey's nails will be done when all coats have been applied and dried, how many minutes will it take her to finish decorating her fingernails and toenails?"""
    num_nails = 20  # Assuming Casey has a total of 20 nails (10 toes + 10 fingers)

    # Time to apply and dry each type of coat
    time_per_coat = 20
    total_time_per_nail = time_per_coat * 3  # Base coat + paint + glitter
    time_between_coats = time_per_coat

    # Total time to finish decorating nails
    total_time = num_nails * (total_time_per_nail + time_between_coats)

    result = total_time
    return result

print(solution())