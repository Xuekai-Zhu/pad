def solution():
    # Define the number of times Jack goes hunting per month
    hunting_frequency = 6

    # Define the number of months in a quarter of the year
    months_in_quarter = 3

    # Calculate the number of times Jack goes hunting in a quarter of the year
    hunting_in_quarter = hunting_frequency * months_in_quarter

    # Calculate the total number of deers Jack catches in a quarter of the year
    total_deers = hunting_in_quarter * 2

    # Calculate the total weight of the deers Jack catches in a quarter of the year
    total_weight = total_deers * 600

    # Calculate how much deer Jack keeps in pounds
    kept_weight = total_weight / 2

    result = kept_weight
    return result

print(solution())