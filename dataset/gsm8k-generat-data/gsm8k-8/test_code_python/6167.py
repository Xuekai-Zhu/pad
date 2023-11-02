def solution():
    # Number of potatoes cut into wedges
    wedges = 13

    # Number of potatoes not cut into wedges
    remaining_potatoes = 67 - wedges

    # Number of potatoes halved
    halved_potatoes = remaining_potatoes / 2

    # Number of potato chips made
    chips = halved_potatoes * 10

    # Number of wedges and chips made
    total = wedges + chips

    # Difference between chips and wedges
    difference = chips - wedges

    result = difference
    return result

print(solution())