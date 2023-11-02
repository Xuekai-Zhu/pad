def solution():
    """Colt and Curt prepared 113 meals to be given away to a charity. Unexpectedly, Sole Mart provided 50 more meals. If Colt and Curt have given 85 meals already, how many more meals are left to be distributed?"""
    # Define the total number of meals prepared
    total_meals = 113

    # Define the number of additional meals provided by Sole Mart
    sole_mart_meals = 50

    # Define the number of meals already distributed
    distributed_meals = 85

    # Calculate the remaining meals to be distributed
    remaining_meals = total_meals + sole_mart_meals - distributed_meals

    # Display the remaining meals
    result = remaining_meals
    return result

print(solution())