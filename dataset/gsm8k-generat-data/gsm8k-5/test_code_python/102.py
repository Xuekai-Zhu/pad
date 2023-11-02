def solution():
    oil_per_wheel = 10  # Ellie needs 10ml of oil to fix each wheel
    oil_rest_of_bike = 5  # Ellie needs 5ml of oil to fix the rest of the bike

    # Calculate the total amount of oil Ellie needs to fix the bike
    total_oil = (2 * oil_per_wheel) + oil_rest_of_bike  # There are 2 wheels on a bike

    result = total_oil
    return result

print(solution())