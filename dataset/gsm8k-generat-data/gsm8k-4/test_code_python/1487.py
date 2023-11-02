def solution():
    """Martin owns a farm with hens. 10 hens do lay 80 eggs in 10 days. Martin decided to buy 15 more hens. How many eggs will all hens lay in 15 days?"""
    # Define the number of hens and eggs produced in 10 days
    initial_hens = 10
    initial_eggs = 80

    # Define the additional number of hens
    additional_hens = 15

    # Calculate the eggs produced per hen per day
    eggs_per_hen_per_day = initial_eggs / (initial_hens * 10)

    # Calculate the total number of hens
    total_hens = initial_hens + additional_hens

    # Calculate the total number of eggs produced in 15 days
    total_eggs = total_hens * eggs_per_hen_per_day * 15

    # Return the result
    result = total_eggs
    return result

print(solution())