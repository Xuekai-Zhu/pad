def solution():
    """Jason joined the military when he turned 18.  It took him 8 years to raise to the rank of chief.  Then 25% longer than that to go from chief to master chief.  He then spent 10 years more in the military before retiring.  How old was he when he retired?"""
    # Define the age at which Jason joined the military
    AGE_AT_JOINING = 18

    # Calculate the age at which Jason became a chief
    age_at_chief = AGE_AT_JOINING + 8

    # Calculate the time it took Jason to go from chief to master chief
    time_from_chief_to_master = 1.25 * 8

    # Calculate the age at which Jason became a master chief
    age_at_master_chief = age_at_chief + time_from_chief_to_master

    # Calculate the age at which Jason retired
    age_at_retirement = age_at_master_chief + 10

    # Display the age at which Jason retired
    result = age_at_retirement
    return result

print(solution())