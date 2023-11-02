def solution():
    grocery_store_distance = 8
    school_distance = 6
    soccer_practice_distance = 12
    total_distance = grocery_store_distance + school_distance + soccer_practice_distance + (2 * school_distance)

    # Calculate the amount of gas required for the trip, assuming a fuel efficiency of 25 mpg
    gas_required = total_distance / 25

    # Calculate the cost of the gas required, assuming a cost of $2.50 per gallon
    gas_cost = gas_required * 2.5
    result = gas_cost
    return result

print(solution())