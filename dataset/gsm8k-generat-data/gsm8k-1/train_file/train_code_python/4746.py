def solution():
    """Dr. Banks had 330 toothbrushes to give away to his patients. He gave away 53 toothbrushes in January. He gave away 67 toothbrushes in February. In March he gave away 46 toothbrushes. In April and May, he gave away the remaining toothbrushes, half each month. How many more toothbrushes did Dr. Banks give out in the busiest month versus the slowest month?"""
    total_toothbrushes = 330
    january_toothbrushes = 53
    february_toothbrushes = 67
    march_toothbrushes = 46
    remaining_toothbrushes = total_toothbrushes - january_toothbrushes - february_toothbrushes - march_toothbrushes
    april_toothbrushes = remaining_toothbrushes / 2
    may_toothbrushes = remaining_toothbrushes / 2
    busiest_month = max(january_toothbrushes, february_toothbrushes, march_toothbrushes, april_toothbrushes, may_toothbrushes)
    slowest_month = min(january_toothbrushes, february_toothbrushes, march_toothbrushes, april_toothbrushes, may_toothbrushes)
    difference = busiest_month - slowest_month
    result = difference
    
    return result

print(solution())