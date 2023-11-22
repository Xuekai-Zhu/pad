def solution():
    
    # Define the prices of blouses, pants, and skirt
    blouse_price = 5
    pant_price = 8
    skirt_price = 6

    # Define the number of blouses, pants, and skirts in the weekly drop-off
    blouses = 5
    pants = 2
    skirts = 1

    # Calculate the total cost of dry-cleaning for 5 weeks
    total_cost = (blouses * blouse_price) + (skirts * skirt_price) + (pants * pant_price)

    # return the result
    result = total_cost
    return result

print(solution())