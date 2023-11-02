def solution():
    initial_jellybeans = 90
    samantha_took = 24
    shelby_ate = 12
    refilled_amount = (samantha_took + shelby_ate) / 2

    # Calculate the current number of jellybeans in the jar
    current_jellybeans = initial_jellybeans - samantha_took - shelby_ate + refilled_amount
    result = current_jellybeans
    return result

print(solution())