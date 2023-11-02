def solution():
    # Define the state of argon and the action of chewing
    argon_state = "gas"
    can_chew_gas = False
    # Check if argon can be chewed
    if argon_state != "solid" and can_chew_gas == False:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())