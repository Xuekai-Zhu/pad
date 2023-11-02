def solution():
    # Find the number of nuts Harry has
    num_harry = 2 * 48

    # Find the number of nuts Bill has
    num_bill = 6 * num_harry

    # Calculate the total number of nuts that Bill and Harry have combined
    total_nuts = num_bill + num_harry
    result = total_nuts
    return result

print(solution())