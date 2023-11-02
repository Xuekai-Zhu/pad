def solution():
    """Casey wants to decorate her toenails and fingernails. First, she wants to do a base coat on each nail, then a coat of paint and finally a coat of glitter on every nail. It takes 20 minutes to apply each coat and 20 minutes for each coat to dry before applying the next one. Assuming Casey's nails will be done when all coats have been applied and dried, how many minutes will it take her to finish decorating her fingernails and toenails?"""
    num_nails = 20
    num_coats = 3
    coat_time = 20
    dry_time = 20
    total_time = num_nails * num_coats * (coat_time + dry_time)
    result = total_time
    return result

print(solution())