def solution():
    cost_per_cut = 100
    months_per_year = 12
    inches_per_month = .5
    inches_to_cut = 4

    #First we need to figure out how many times he will need to cut his grass in a year
    #2 inch grass + .5 inch growth per month = 4 inches.  This is when he will need to cut his grass.
    #4 inches - 2 inches (initial height) = 2 inches that need to be cut.
    #Since the growth is .5 inches per month, it will take 4 months for the grass to reach 4 inches (2 inches + 2 inches of growth)
    #2 inches (height to cut) / .5 inches (growth per month) = 4 months

    # This means that he will need to cut his grass 3 times a year.
    cuts_per_year = months_per_year / 4

    # Now we need to figure out how much it will cost him per year to get his grass cut.
    cost_per_year = cost_per_cut * cuts_per_year

    result = cost_per_year

    return

print(solution())