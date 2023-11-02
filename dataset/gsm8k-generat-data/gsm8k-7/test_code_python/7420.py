def solution():
    num_ants = 400
    ant_food_per_ant = 2
    cost_per_ounce = 0.1

    total_ant_food = num_ants * ant_food_per_ant
    total_cost = total_ant_food * cost_per_ounce

    num_leaves_raked = 6000
    cost_per_job = 5 + (num_leaves_raked * 0.01)

    num_jobs_needed = total_cost / cost_per_job
    result = num_jobs_needed
    return result

print(solution())