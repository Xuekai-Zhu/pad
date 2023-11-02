def solution():
    """Martin owns a farm with hens. 10 hens do lay 80 eggs in 10 days. Martin decided to buy 15 more hens. How many eggs will all hens lay in 15 days?"""
    # Define the number of hens and eggs laid in 10 days for every 10 hens
    hens_per_10 = 10
    eggs_per_10_days = 80

    # Calculate the total number of hens after buying 15 more
    total_hens = hens_per_10 + 15

    # Calculate the number of eggs laid by one hen in 15 days
    eggs_per_hen = eggs_per_10_days / 10 * 1.5

    # Calculate the total number of eggs laid by all hens in 15 days
    total_eggs = total_hens * eggs_per_hen * 15

    # Display the total number of eggs
    result = total_eggs
    return result

print(solution())