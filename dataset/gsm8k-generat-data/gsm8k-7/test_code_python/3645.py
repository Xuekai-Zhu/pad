def solution():
    car_commutes = 3
    motorcycle_commutes = 2

    car_toll = 12.5
    motorcycle_toll = 7

    car_mpg = 35
    motorcycle_mpg = 35

    commute_distance = 14
    gas_price = 3.75

    # Calculate the total distance driven by car and motorcycle
    total_distance = (car_commutes + motorcycle_commutes) * commute_distance

    # Calculate the total gas used by car and motorcycle
    total_gas_used = (car_commutes * (commute_distance / car_mpg)) + (motorcycle_commutes * (commute_distance / motorcycle_mpg))

    # Calculate the total cost of gas for the week
    total_gas_cost = total_gas_used * gas_price

    # Calculate the total cost of tolls for the week
    total_toll_cost = (car_commutes * car_toll) + (motorcycle_commutes * motorcycle_toll)

    # Calculate the total cost of driving to work and back for the week
    total_cost = total_gas_cost + total_toll_cost
    result = total_cost
    return result

print(solution())