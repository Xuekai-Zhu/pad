def solution():
    """Nikola is saving up for a bag of ant food before he can start his ant farm. He wants 400 ants in his farm. Each ant needs 2 ounces of food. Every ounce of ant food costs $.1. Nikola is saving up by raking leaves. He charges $5 to start a job and then he charges by the leaf. Each leaf he rakes costs 1 penny. He finally saved up enough money after he raked 6,000 leaves. How many jobs did he complete?"""
    # Define the number of ants and the amount of food they need
    ants = 400
    food_amount = ants * 2

    # Define the cost of ant food
    food_cost = food_amount * 0.1

    # Define the cost to start a job
    job_cost = 5

    # Define the amount earned per leaf
    leaf_cost = 0.01

    # Define the total amount earned from raking leaves
    leaf_earnings = 6000 * leaf_cost

    # Calculate the total amount saved by Nikola
    total_savings = leaf_earnings + job_cost

    # Check if Nikola can afford the ant food
    if total_savings >= food_cost:
        # Calculate the number of jobs completed
        jobs_completed = (total_savings - food_cost) / job_cost
    else:
        jobs_completed = 0

    # Return the result
    result = int(jobs_completed)
    return result

print(solution())