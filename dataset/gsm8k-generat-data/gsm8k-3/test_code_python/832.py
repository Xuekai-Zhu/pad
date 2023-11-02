def solution():
    """John buys 1000 balloons. Each balloon holds 10 liters of air. If he buys 500-liter tanks of gas, how many tanks does he need to buy to fill all the balloons?"""
    # Calculate the total number of liters of air needed
    total_liters = 1000 * 10

    # Calculate the number of 500-liter tanks needed
    num_tanks = total_liters // 500
    if total_liters % 500 != 0:
        num_tanks += 1

    # Display the number of tanks needed
    result = num_tanks
    return result

print(solution())