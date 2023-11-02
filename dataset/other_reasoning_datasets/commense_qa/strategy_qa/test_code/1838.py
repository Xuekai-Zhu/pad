def solution():
    is_pruno_made_in_prisons = True
    does_prison_environment_allow_brewing = True
    if is_pruno_made_in_prisons and does_prison_environment_allow_brewing:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())