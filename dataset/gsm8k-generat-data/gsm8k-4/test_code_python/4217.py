def solution():
    """A group of 30 tourists sets out on a walking tour of the rainforest. Two tourists are eaten by anacondas, then half the remaining tourists try to pet poisonous dart frogs and get poisoned. If only 1/7 of the poisoned tourists recovered, how many tourists are left at the end of the tour?"""
    # Define the initial number of tourists
    initial_tourists = 30

    # Calculate the number of tourists eaten by anacondas
    eaten_tourists = 2

    # Calculate the number of remaining tourists
    remaining_tourists = initial_tourists - eaten_tourists

    # Calculate the number of tourists poisoned by dart frogs
    poisoned_tourists = remaining_tourists / 2

    # Calculate the number of tourists who recovered
    recovered_tourists = poisoned_tourists / 7

    # Calculate the number of tourists left at the end of the tour
    end_tourists = remaining_tourists - poisoned_tourists + recovered_tourists

    # return the result
    result = end_tourists
    return result

print(solution())