def solution():
    # Calculate the total number of pounds of lobster in the other two harbors
    total_lobster = 80 + 80

    # Calculate the total number of pounds of lobster in Hooper Bay
    hooper_bay_lobster = total_lobster * 2

    # Calculate the total number of pounds of lobster in all three harbors
    total_lobster = total_lobster + hooper_bay_lobster
    result = total_lobster
    return result

print(solution())