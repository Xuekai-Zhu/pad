def solution():
    plessy_v_ferguson_decision = "segregation did not violate the constitution"
    wilson_discriminatory_hiring_policies = True
    wilson_segregated_government_offices = True
    # Check if Wilson's actions align with the Plessy v. Ferguson decision
    if plessy_v_ferguson_decision in wilson_discriminatory_hiring_policies and wilson_segregated_government_offices:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())