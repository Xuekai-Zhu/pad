def solution():
    """A salesman bought a case of 48 backpacks for $576. He sold 17 of them for $18 at the swap meet, 10 were sold to a department store for $25 each. If the remainder were sold for $22 each. How much was the salesman's profit?"""
    # Define the initial cost to purchase the backpacks
    INITIAL_COST = 576

    # Define the number of backpacks in the case
    BACKPACKS_IN_CASE = 48

    # Define the number of backpacks sold at the swap meet, department store, and the remaining
    sold_swap_meet = 17
    sold_dept_store = 10
    sold_remaining = BACKPACKS_IN_CASE - sold_swap_meet - sold_dept_store

    # Calculate the total earnings from selling the backpacks
    earnings_swap_meet = sold_swap_meet * 18
    earnings_dept_store = sold_dept_store * 25
    earnings_remaining = sold_remaining * 22
    total_earnings = earnings_swap_meet + earnings_dept_store + earnings_remaining

    # Calculate the total cost of purchasing the backpacks
    total_cost = INITIAL_COST

    # Calculate the profit
    profit = total_earnings - total_cost

    # Return the profit
    result = profit
    return result

print(solution())