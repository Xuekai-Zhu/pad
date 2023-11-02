def solution():
    # Define the gas station prices
    price1 = 3
    price2 = 3.5
    price3 = 4
    price4 = 4.5

    # Define the size of Tara's gas tank
    gas_tank_size = 12

    # Calculate the total cost of gas for each fill-up
    fillup1_cost = price1 * gas_tank_size
    fillup2_cost = price2 * gas_tank_size
    fillup3_cost = price3 * gas_tank_size
    fillup4_cost = price4 * gas_tank_size

    # Calculate the total amount spent on gas
    total_gas_cost = fillup1_cost + fillup2_cost + fillup3_cost + fillup4_cost

    result = total_gas_cost
    return result

print(solution())