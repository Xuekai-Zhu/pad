def solution():
    base_price = 45  # Chris pays a base price of $45 for 100 GB
    total_price = 65  # Chris's bill for this month is $65

    # Calculate the number of additional GB Chris was charged for
    extra_gb = (total_price - base_price) / 0.25

    result = extra_gb
    return result

print(solution())