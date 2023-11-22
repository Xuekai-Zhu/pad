def solution():
    
    # Define the prices of the material and jeweler
    material_price = 500
    jeweler_price = 800

    # Calculate the total cost of the brooch
    total_cost = material_price + jeweler_price

    # Calculate the amount Janet pays for getting the insured
    insured_cost = total_cost * 0.1

    # Calculate the amount Janet pays back
    back_cost = total_cost - insured_cost

    # Display the amount Janet pays back
    result = back_cost
    return result

print(solution())