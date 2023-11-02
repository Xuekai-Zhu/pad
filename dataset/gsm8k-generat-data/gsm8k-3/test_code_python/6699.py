def solution():
    """Bob has to hire someone to fix his garden.  A storm destroyed all 20 of his rose bushes.  He decides to replant all the rose bushes.  Each rose bush costs $150.  He also needs to pay a gardener $30 an hour, 5 hours each day for 4 days.  The final expense is 100 cubic feet of soil sold for $5 per cubic foot.  How much did the entire gardening project cost?"""
    # Define the cost of each rose bush and the number of rose bushes needed
    ROSE_BUSH_COST = 150
    NUM_ROSE_BUSHES = 20

    # Calculate the total cost of the rose bushes
    rose_bush_cost = ROSE_BUSH_COST * NUM_ROSE_BUSHES

    # Define the gardener's hourly rate and the number of hours worked
    HOURLY_RATE = 30
    NUM_HOURS = 5 * 4

    # Calculate the total cost of the gardener
    gardener_cost = HOURLY_RATE * NUM_HOURS

    # Define the cost per cubic foot of soil and the amount of soil needed
    SOIL_COST = 5
    SOIL_AMOUNT = 100

    # Calculate the total cost of the soil
    soil_cost = SOIL_COST * SOIL_AMOUNT

    # Calculate the total cost of the entire gardening project
    total_cost = rose_bush_cost + gardener_cost + soil_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())