def solution():
    """A group of 30 tourists sets out on a walking tour of the rainforest. Two tourists are eaten by anacondas, then half the remaining tourists try to pet poisonous dart frogs and get poisoned. If only 1/7 of the poisoned tourists recovered, how many tourists are left at the end of the tour?"""
    # Define the initial number of tourists
    num_tourists = 30

    # Two tourists are eaten by anacondas
    num_tourists -= 2

    # Half the remaining tourists try to pet poisonous dart frogs and get poisoned
    num_tourists /= 2

    # Define the number of poisoned tourists and calculate the number of recovered tourists
    num_poisoned = int(num_tourists)
    num_recovered = num_poisoned // 7

    # Calculate the number of tourists remaining at the end of the tour
    num_remaining = num_tourists - num_poisoned + num_recovered

    # Display the number of tourists remaining
    result = num_remaining
    return result

print(solution())