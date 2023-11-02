def solution():
    """Dr. Banks had 330 toothbrushes to give away to his patients. He gave away 53 toothbrushes in January. He gave away 67 toothbrushes in February. In March he gave away 46 toothbrushes. In April and May, he gave away the remaining toothbrushes, half each month. How many more toothbrushes did Dr. Banks give out in the busiest month versus the slowest month?"""
    # Initialize the number of toothbrushes given away in each month
    january = 53
    february = 67
    march = 46

    # Calculate the number of toothbrushes given away in April and May
    remaining = 330 - january - february - march
    april = remaining // 2
    may = remaining - april

    # Find the busiest and slowest months
    busiest = max(january, february, march, april, may)
    slowest = min(january, february, march, april, may)

    # Calculate the difference between the busiest and slowest months
    difference = busiest - slowest

    # Return the result
    result = difference
    return result

print(solution())