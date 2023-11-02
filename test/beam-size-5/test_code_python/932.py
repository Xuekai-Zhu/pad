def solution():
    # Calculate the total number of pesos added after 12 hours
    added_tesos_12_hours = 70 * 12

    # Calculate the total number of pesos added after 24 hours
    added_tesos_24_hours = 70 * 24

    # Calculate the total number of pesos added after 5 pm
    total_added_tesos = added_tesos_12_hours + added_tesos_24_hours

    # Calculate the total amount of money saved by Cameron
    amount_saved = total_added_tesos - 1000 - 1600
    result = amount_saved
    return result

print(solution())