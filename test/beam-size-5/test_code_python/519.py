def solution():
    
    # Define the initial number of loaves of bread
    initial_loaves = 200

    # Calculate the number of loaves sold in the morning
    morning_loaves = 93

    # Calculate the number of loaves sold in the afternoon
    afternoon_loaves = 39

    # Calculate the total number of loaves sold
    total_loaves_sold = morning_loaves + afternoon_loaves

    # Calculate the number of loaves returned by the grocery store
    grocery_loaves = 6

    # Calculate the number of loaves left
    loaves_left = initial_loaves - total_loaves_sold - grocery_loaves

    # Display the number of loaves left
    result = loaves_left
    return result

print(solution())