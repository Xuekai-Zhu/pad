def solution():
    
    # Define the initial number of lollipops
    initial_lollipops = 7

    # Define the number of lollipops Erin's mother gives Erin
    mother_lollipops = 10

    # Define the number of lollipops Erin gives to Ella
    ella_lollipops = 3

    # Calculate the number of lollipops Erin has left
    remaining_lollipops = initial_lollipops - mother_lollipops - ella_lollipops

    # Display the number of lollipops Erin has left
    result = remaining_lollipops
    return result

print(solution())