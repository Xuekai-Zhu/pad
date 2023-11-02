def solution():
    """Rebecca runs a hair salon. She charges $30 for haircuts, $40 for perms, and $60 for dye jobs, but she has to buy a box of hair dye for $10 to dye every head of hair. Today, she has four haircuts, one perm, and two dye jobs scheduled. If she makes $50 in tips, how much money will she have in dollars at the end of the day?"""
    haircuts = 4
    perms = 1
    dye_jobs = 2
    haircut_income = haircuts * 30
    perm_income = perms * 40
    dye_job_income = dye_jobs * 60
    dye_job_costs = dye_jobs * 10
    total_income = haircut_income + perm_income + dye_job_income - dye_job_costs + 50
    result = total_income
    return result

print(solution())