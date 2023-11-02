def solution():
    # Define the catch rate and number of hours
    catch_rate = 7
    hours_fishing = 9

    # Calculate the total catch before any losses
    total_catch = catch_rate * hours_fishing

    # Subtract the number of lost fish
    total_catch -= 15

    result = total_catch
    return result

print(solution())