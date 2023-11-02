def solution():
    start_age = 18  # Jason joined the military when he turned 18
    years_to_chief = 8  # It took him 8 years to raise to the rank of chief
    years_to_master_chief = int(1.25 * years_to_chief)  # 25% longer than that to go from chief to master chief
    years_after_master = 10  # He spent 10 years more in the military after becoming a master chief

    # Calculate Jason's age when he became a chief
    age_at_chief = start_age + years_to_chief

    # Calculate Jason's age when he became a master chief
    age_at_master_chief = age_at_chief + years_to_master_chief

    # Calculate Jason's age at retirement
    age_at_retirement = age_at_master_chief + years_after_master
    result = age_at_retirement
    return result

print(solution())