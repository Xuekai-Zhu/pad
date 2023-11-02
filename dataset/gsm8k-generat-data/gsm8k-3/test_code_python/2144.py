def solution():
    """Sharon’s vacation rental has a Keurig coffee machine.  She will be there for 40 days.  She has 3 cups of coffee (3 coffee pods) every morning.
    Her coffee pods come 30 pods to a box for $8.00.  How much will she spend on coffee to last her for the entire vacation?"""
    # Define the number of pods Sharon needs per day and the number of days she will be on vacation
    PODS_PER_DAY = 3
    NUM_DAYS = 40

    # Define the number of pods per box and the cost per box
    PODS_PER_BOX = 30
    COST_PER_BOX = 8.0

    # Calculate the total number of pods Sharon needs for the entire vacation
    total_pods = PODS_PER_DAY * NUM_DAYS

    # Calculate the total number of boxes Sharon needs to buy
    boxes_needed = total_pods // PODS_PER_BOX
    if total_pods % PODS_PER_BOX != 0:
        boxes_needed += 1

    # Calculate the total cost of the coffee pods
    total_cost = boxes_needed * COST_PER_BOX

    # Display the total cost
    result = total_cost
    return result

print(solution())