def solution():
    
    # Define the initial price of the toy
    price = 40

    # In December, the price increased by 80%
    price *= 1.8

    # In January, the price decreased by 50%
    price *= 0.5

    # Display the final price of the toy
    result = price
    return result

print(solution())