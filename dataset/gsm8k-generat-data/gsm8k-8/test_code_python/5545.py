def solution():
    # Define the number of plants needed for each pot
    fern = 1
    creeping_jennies = 4
    geraniums = 4

    # Calculate the cost per pot
    fern_cost = fern * 15.00
    creeping_jennies_cost = creeping_jennies * 4.00
    geraniums_cost = geraniums * 3.50

    # Calculate the total cost for all pots
    total_cost = (fern_cost + creeping_jennies_cost + geraniums_cost) * 4

    result = total_cost
    return result

print(solution())