def solution():
    """A bond paper ream has 500 sheets and costs $27. An office needs 5000 sheets of bond paper. How much will it cost to buy their needed sheets of paper?"""
    # Define the number of sheets per ream and the cost per ream
    SHEETS_PER_REAM = 500
    REAM_COST = 27

    # Determine how many reams are needed to get 5000 sheets
    reams_needed = 5000 // SHEETS_PER_REAM  # Use floor division to get the whole number of reams needed

    # Calculate the total cost of the needed reams
    total_cost = reams_needed * REAM_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())