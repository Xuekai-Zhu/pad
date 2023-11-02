def solution():
    """Carlson bought land that cost $8000 and additional land that cost $4000. He initially owned 300 square meters of land. If the land he bought costs $20 per square meter, how big is his land after buying the new land?"""
    # Define the cost per square meter of land
    COST_PER_SQM = 20

    # Define the cost of the land Carlson bought
    cost_bought = 8000 + 4000

    # Calculate the size of the land Carlson bought
    size_bought = cost_bought / COST_PER_SQM

    # Calculate the total size of Carlson's land
    total_size = size_bought + 300

    # Display the total size of Carlson's land
    result = total_size
    return result

print(solution())