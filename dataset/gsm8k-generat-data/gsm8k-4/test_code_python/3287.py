def solution():
    """Jason is hiring two construction workers, one electrician and one plumber. If the construction workers each make $100/day, the electrician makes double what a worker is paid and the plumber makes 250% of a worker's salary, how much are the overall labor costs for one day?"""
    # Define the daily wage of a construction worker
    construction_wage = 100

    # Calculate the daily wage of the electrician and the plumber
    electrician_wage = construction_wage * 2
    plumber_wage = construction_wage * 2.5

    # Calculate the total labor cost per day
    total_cost = (2 * construction_wage) + electrician_wage + plumber_wage

    result = total_cost
    return result

print(solution())