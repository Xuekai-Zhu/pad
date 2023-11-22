def solution():
    
    # Define the initial number of loaves of bread
    initial_loaves = 200

    # Define the number of loaves sold in the morning and afternoon
    morning_sold = 93
    afternoon_sold = 39

    # Define the number of unsold loaves
    unsold_loaves = 6

    # Calculate the total number of loaves sold
    total_sold = morning_sold + afternoon_sold

    # Calculate the number of loaves left after the grocery store returns some
    remaining_loaves = initial_loaves - total_sold - unsold_loaves

    # return the result
    result = remaining_loaves
    return result

print(solution())