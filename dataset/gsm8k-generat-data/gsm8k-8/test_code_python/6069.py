def solution():
    # Define Mia and Billy's egg decorating rates
    mia_rate = 2 * 12
    billy_rate = 10

    # Calculate the combined egg decorating rate
    combined_rate = mia_rate + billy_rate

    # Calculate the time it will take to decorate all the eggs
    time_to_decorate = 170 / combined_rate
    result = time_to_decorate
    return result

print(solution())