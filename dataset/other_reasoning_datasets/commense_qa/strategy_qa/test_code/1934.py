def solution():
    # Define the location of Des Moines and the requirement for surfing
    des_moines_state = "Iowa"
    surfing_requirement = "waves at a beach or ocean"
    # Check if Des Moines is located in a state with beaches or oceans for surfing
    if des_moines_state != "California" and des_moines_state != "Hawaii" and des_moines_state != "Florida":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())