def solution():
    """Nikola is saving up for a bag of ant food before he can start his ant farm. He wants 400 ants in his farm. Each ant needs 2 ounces of food. Every ounce of ant food costs $.1. Nikola is saving up by raking leaves. He charges $5 to start a job and then he charges by the leaf. Each leaf he rakes costs 1 penny. He finally saved up enough money after he raked 6,000 leaves. How many jobs did he complete?"""
    ants_needed = 400
    ounces_per_ant = 2
    cost_per_ounce = 0.1
    total_food_cost = ants_needed * ounces_per_ant * cost_per_ounce
    leaves_raked = 6000
    cost_per_leaf = 0.01
    leaf_cost = leaves_raked * cost_per_leaf
    total_cost = total_food_cost + leaf_cost + 5
    jobs_completed = total_cost / 25 # assuming Nikola charges $25 per job
    result = jobs_completed
    return result

print(solution())