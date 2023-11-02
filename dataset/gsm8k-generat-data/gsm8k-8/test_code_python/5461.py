def solution():
    # Calculate the number of clovers with 3 petals
    three_petals = 0.75 * 200

    # Calculate the number of clovers with 2 petals
    two_petals = 0.24 * 200

    # Calculate the number of clovers with 4 petals
    four_petals = 0.01 * 200

    # Calculate the total number of petals on the clovers with 3 petals
    total_petals_three = three_petals * 3

    # Calculate the total number of petals on the clovers with 2 petals
    total_petals_two = two_petals * 2

    # Calculate the total number of petals on the clovers with 4 petals
    total_petals_four = four_petals * 4

    # Calculate the total number of petals on all the clovers
    total_petals = total_petals_three + total_petals_two + total_petals_four

    # Calculate how much June earns in cents
    earnings = total_petals

    return earnings

print(solution())