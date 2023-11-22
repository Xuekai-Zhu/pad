def solution():
    
    # Define the prices of pencils and erasers
    pencil_price = 0.5
    eraser_price = 0.25

    # Define the number of pencils and erasers purchased
    num_pencils = 6
    num_erasers = 8

    # Calculate the total cost of the purchase
    total_cost = (pencil_price * num_pencils) + (eraser_price * num_erasers)

    # Calculate the change
    change = 10 - total_cost

    # return the result
    result = change
    return result

print(solution())