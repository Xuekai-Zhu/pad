def solution():
    num_passengers = 80
    num_men = 30

    # Calculate the number of women on the airplane
    num_women = num_passengers / 2 - num_men

    # Calculate the number of children on the airplane
    num_children = num_passengers - num_men - num_women
    result = num_children
    return result

print(solution())