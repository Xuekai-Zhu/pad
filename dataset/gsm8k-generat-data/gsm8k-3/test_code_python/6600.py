def solution():
    """Chef Michel made shepherd's pie cut into 4 pieces and chicken pot pie cut into 5 pieces for the lunch crowd.  52 customers ordered slices of shepherd's pie and 80 customers ordered slices of chicken pot pie. How many total pies did Chef Michel sell?"""
    # Define the number of customers who ordered each type of pie
    shepherd_customers = 52
    chicken_customers = 80

    # Calculate the total number of slices of each type of pie ordered
    shepherd_slices = shepherd_customers * 4
    chicken_slices = chicken_customers * 5

    # Calculate the total number of pies sold
    total_pies = (shepherd_slices + chicken_slices) // (4 + 5)

    # Display the total number of pies sold
    result = total_pies
    return result

print(solution())