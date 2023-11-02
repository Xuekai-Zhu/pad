def solution():
    harbor_1 = 80 # pounds of lobster
    harbor_2 = 80 # pounds of lobster

    # Calculate total pounds of lobster in both harbors combined
    total_lobster_in_two_harbors = harbor_1 + harbor_2

    # Calculate pounds of lobster in Hooper Bay
    hooper_bay = total_lobster_in_two_harbors * 2

    # Calculate total pounds of lobster in all three harbors
    total_lobster = harbor_1 + harbor_2 + hooper_bay
    result = total_lobster
    return result

print(solution())