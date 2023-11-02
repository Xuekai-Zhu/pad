def solution():
    """A chef needs to make french fries.  He can get 25 fries out of 1 potato.  He has 15 potatoes and he needs 200 fries.  How many potatoes will he have leftover?"""
    # Define the number of fries per potato and the number of available potatoes
    fries_per_potato = 25
    available_potatoes = 15

    # Calculate the total number of fries that can be made with the available potatoes
    total_fries = fries_per_potato * available_potatoes

    # Calculate the number of leftover fries
    leftover_fries = total_fries - 200

    # Calculate the number of leftover potatoes
    leftover_potatoes = int(leftover_fries / fries_per_potato)

    # Display the number of leftover potatoes
    result = leftover_potatoes
    return result

print(solution())