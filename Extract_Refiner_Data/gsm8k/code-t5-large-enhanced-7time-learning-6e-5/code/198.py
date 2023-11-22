def solution():
    
    # Define the number of acres and the number of tons of grapes produced per acre per year
    acres = 10
    tons_per_acre = 5

    # Calculate the total number of tons of grapes produced per year
    total_tures = acres * tons_per_acre

    # Calculate the total number of barrels of wine produced per year
    barrels_per_ton = total_tures * 2

    # Display the total number of barrels of wine produced per year
    result = barrels_per_ton
    return result

print(solution())