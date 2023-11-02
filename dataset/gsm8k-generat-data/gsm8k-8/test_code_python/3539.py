def solution():
    # Calculate Rupert's age relative to Peter's
    rupert_to_peter_ratio = 3.5
    age_difference_ratio = 1 + rupert_to_peter_ratio
    total_age_ratio = 2

    # Solve for Peter's age
    peter_age = 10 / age_difference_ratio

    # Solve for Rupert's age
    rupert_age = peter_age * rupert_to_peter_ratio

    # Calculate the number of candles on Rupert's cake
    candles_on_rupert_cake = round((rupert_age / total_age_ratio) * 10)

    result = candles_on_rupert_cake
    return result

print(solution())