def solution():
    haircut_price = 30
    perm_price = 40
    dye_job_price = 60
    cost_of_hair_dye = 10

    num_haircuts = 4
    num_perms = 1
    num_dye_jobs = 2
    tip_amount = 50

    # Calculate the total revenue from haircuts
    total_haircut_revenue = num_haircuts * haircut_price

    # Calculate the total revenue from perms
    total_perm_revenue = num_perms * perm_price

    # Calculate the total revenue from dye jobs
    total_dye_job_revenue = num_dye_jobs * dye_job_price

    # Calculate the total cost of hair dye
    total_hair_dye_cost = num_dye_jobs * cost_of_hair_dye

    # Calculate the total revenue for the day
    total_revenue = total_haircut_revenue + total_perm_revenue + total_dye_job_revenue - total_hair_dye_cost + tip_amount

    result = total_revenue
    return result

print(solution())