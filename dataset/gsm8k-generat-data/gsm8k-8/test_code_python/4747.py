def solution():
    # Define the initial number of toothbrushes
    initial_toothbrushes = 330

    # Define the number of toothbrushes given away each month
    january_toothbrushes = 53
    february_toothbrushes = 67
    march_toothbrushes = 46

    # Calculate the remaining toothbrushes after March
    remaining_toothbrushes = initial_toothbrushes - january_toothbrushes - february_toothbrushes - march_toothbrushes
    april_toothbrushes = remaining_toothbrushes / 2
    may_toothbrushes = remaining_toothbrushes / 2

    # Calculate the busiest and slowest months
    busiest_month = max(january_toothbrushes, february_toothbrushes, march_toothbrushes, april_toothbrushes, may_toothbrushes)
    slowest_month = min(january_toothbrushes, february_toothbrushes, march_toothbrushes, april_toothbrushes, may_toothbrushes)

    # Calculate the difference between the busiest and slowest months
    difference = busiest_month - slowest_month

    result = difference
    return result

print(solution())