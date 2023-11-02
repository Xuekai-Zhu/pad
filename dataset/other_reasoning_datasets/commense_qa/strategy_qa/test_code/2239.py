def solution():
    # Define the fact that living organ donors can donate their spare kidney
    living_donors_can_donate_kidney = True
    # Check if a donor needs to be dead to donate a kidney
    if not living_donors_can_donate_kidney:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())