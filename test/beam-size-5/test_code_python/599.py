def solution():
    # Calculate the total amount of chocolates made by Ruiz in 12 hours
    luiz_chocolates = 120 * 2

    # Calculate the amount of chocolates made by Marissa in 12 hours
    marissa_chocolates = (3/4) * luiz_chocolates * 12

    # Calculate the total amount of chocolates made by both of them
    total_chocolates = luiz_chocolates + marissa_chocolates
    result = total_chocolates
    return result

print(solution())