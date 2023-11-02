def solution():
    """If Pam is currently twice as young as Rena is, and in 10 years Rena will be 5 years older than her, how old is Pam now?"""
    pam_age_ratio = 1/2
    rena_age_increase = 5
    total_age_increase = 2*rena_age_increase
    pam_age = total_age_increase/(1+2) #Pam is 1/3 the age of Rena
    result = pam_age
    return result

print(solution())