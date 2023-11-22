def solution():
    
    # Define the number of cars Jason needs to sell and the average number of customers
    cars_needed = 15
    customers_average = (cars_needed // 25) + (cars_needed % 25 > 0)

    # Calculate the number of telephone calls Jason needs to make based on the average number of customers
    calls_needed = (customers_average * 2) // 25

    # return the result
    result = calls_needed
    return result

print(solution())