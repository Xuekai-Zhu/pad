def solution():
    initial_stock = 55
    restocked = 132
    final_stock = 164

    # Calculate the number of bags sold
    sold = initial_stock + restocked - final_stock
    result = sold
    return result

print(solution())