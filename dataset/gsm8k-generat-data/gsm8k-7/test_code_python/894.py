def solution():
    num_quarters = 35
    state_quarters_fraction = 2/5
    pa_state_quarters_fraction = 0.50

    # Calculate the number of state quarters Nick has
    num_state_quarters = num_quarters * state_quarters_fraction

    # Calculate the number of Pennsylvania state quarters Nick has
    num_pa_quarters = num_state_quarters * pa_state_quarters_fraction
    result = num_pa_quarters
    return result

print(solution())