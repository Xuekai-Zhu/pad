def solution():
    group_size = 30  # There are 30 tourists in the group
    anaconda_victims = 2  # Two tourists are eaten by anacondas
    remaining_tourists = group_size - anaconda_victims  # Remaining tourists

    poisoned_tourists = remaining_tourists / 2  # Half of the remaining tourists get poisoned by dart frogs
    recovered_tourists = poisoned_tourists / 7  # Only 1/7 of the poisoned tourists recovered

    # Calculate the total tourists left at the end of the tour
    total_tourists_left = remaining_tourists - poisoned_tourists + recovered_tourists
    result = total_tourists_left
    return result

print(solution())