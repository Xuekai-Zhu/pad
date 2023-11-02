def solution():
    
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