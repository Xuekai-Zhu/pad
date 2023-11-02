def solution():
    # Define the total distance traveled by Luisa
    total_distance = 10 + 6 + 5 + 9

    # Calculate the number of gallons needed
    gallons_needed = total_distance / 15

    # Calculate the total cost of gas
    gas_cost = gallons_needed * 3.50

    result = gas_cost
    return result

print(solution())