def solution():
    # Calculate the total number of coffee pods needed for the entire vacation
    total_coffee_pods = 3 * 40

    # Calculate the number of boxes needed, rounding up to the nearest whole number
    boxes_needed = int((total_coffee_pods + 29) / 30)

    # Calculate the total cost of the coffee
    total_cost = boxes_needed * 8

    result = total_cost
    return result

print(solution())