def solution():
    
    # Define the amount of chocolates Ruiz can make in two hours
    luiz_chocolates = 120

    # Define the amount of chocolates Marissa can make in one hour
    marissa_chocolates = (3/4) * luiz_chocolates

    # Calculate the total amount of chocolates made in 12 hours
    total_chocolates = (luiz_chocolates + marissa_chocolates) * 12

    # Display the total amount of chocolates made
    result = total_chocolates
    return result

print(solution())