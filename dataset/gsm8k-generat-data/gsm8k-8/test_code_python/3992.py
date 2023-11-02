def solution():
    # Calculate the total pounds of lobster at the other two harbors
    total_other_two_harbors = 80 + 80

    # Calculate the pounds of lobster at Hooper Bay
    hooper_bay = total_other_two_harbors * 2

    # Calculate the total pounds of lobster at all three harbors
    total_pounds_of_lobster = total_other_two_harbors + hooper_bay
    result = total_pounds_of_lobster
    return result

print(solution())