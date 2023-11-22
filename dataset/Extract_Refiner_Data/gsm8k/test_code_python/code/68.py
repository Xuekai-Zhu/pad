def solution():
    
    # Define the prices and number of slices
    brownie_price = 3
    cheesecake_price = 4
    brownie_slices = 43
    cheesecake_slices = 23

    # Calculate the total amount raised
    total_raised = (brownie_price * brownie_slices) + (cheesecake_price * cheesecake_slices)

    # return the result
    result = total_raised
    return result

print(solution())