def solution():
    
    # Define the initial number of fries
    griffin_fries = 24

    # Calculate the number of fries Kyle took
    kyle_fries = 5

    # Calculate the number of fries Billy took
    billy_fries = kyle_fries * 2

    # Calculate the number of fries Ginger took
    ginger_fries = kyle_fries + billy_fries + 3

    # Calculate the number of fries Ginger gave Griffin
    ginger_fries += 27

    # Display the number of fries Ginger gave Griffin
    result = ginger_fries
    return result

print(solution())