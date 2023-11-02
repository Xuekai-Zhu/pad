def solution():
    """Nikola is saving up for a bag of ant food before he can start his ant farm. He wants 400 ants in his farm. Each ant needs 2 ounces of food. Every ounce of ant food costs $.1. Nikola is saving up by raking leaves. He charges $5 to start a job and then he charges by the leaf. Each leaf he rakes costs 1 penny. He finally saved up enough money after he raked 6,000 leaves. How many jobs did he complete?"""
    ant_count = 400
    food_per_ant = 2
    food_cost_per_ounce = 0.1
    total_food_cost = ant_count * food_per_ant * food_cost_per_ounce
    leaves_needed = total_food_cost * 100 / 5
    leaves_per_job = 6000
    jobs_completed = int((leaves_needed - leaves_per_job + 1) / leaves_per_job)
    result = jobs_completed
    return result

print(solution())