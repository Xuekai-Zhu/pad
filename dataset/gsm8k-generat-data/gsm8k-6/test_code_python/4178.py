def solution():
    # Calculate the total amount of time John spends on his PhD
    acclimation_period = 1
    basics_period = 2
    research_period = 2.75 * basics_period  # John spends 75% more time on research than he did learning the basics
    writing_period = acclimation_period / 2   # John spends half as long on writing his dissertation as his acclimation period
    total_period = acclimation_period + basics_period + research_period + writing_period
    result = total_period
    return result

print(solution())