def solution():
    """Jason joined the military when he turned 18. It took him 8 years to raise to the rank of chief. Then 25% longer than that to go from chief to master chief. He then spent 10 years more in the military before retiring. How old was he when he retired?"""
    # Define the age when Jason joined the military
    age_at_joining = 18

    # Calculate the age when Jason became a chief
    age_at_chief = age_at_joining + 8

    # Calculate the time it took Jason to go from chief to master chief
    time_to_master = 1.25 * 8

    # Calculate the age when Jason became a master chief
    age_at_master = age_at_chief + time_to_master

    # Calculate the age when Jason retired
    age_at_retirement = age_at_master + 10

    # Return the age at retirement
    result = age_at_retirement
    return result

print(solution())