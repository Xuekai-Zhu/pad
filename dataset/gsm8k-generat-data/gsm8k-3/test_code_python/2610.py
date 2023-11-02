def solution():
    """A farmer has 46 chickens. Each chicken gives him 6 eggs a week. If he sells a dozen eggs for $3, how much money would he make in 8 weeks?"""
    # Define the number of chickens
    num_chickens = 46

    # Define the number of weeks
    num_weeks = 8

    # Calculate the total number of eggs produced
    total_eggs = num_chickens * 6 * num_weeks

    # Calculate the number of dozens of eggs produced
    dozens_of_eggs = total_eggs / 12

    # Calculate the total revenue from selling the eggs
    total_revenue = dozens_of_eggs * 3

    # Display the total revenue
    result = total_revenue
    return result

print(solution())