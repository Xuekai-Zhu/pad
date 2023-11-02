def solution():
    # Convert euros to pounds
    euros_to_pounds = 2 * 11  # 2 pounds per euro
    total_pounds = 42 + euros_to_pounds + (3000/100)  # add pounds, euros and converted yen

    # Convert total pounds to yen
    total_yen = total_pounds * 100  # 100 yen per pound
    result = total_yen
    return result

print(solution())