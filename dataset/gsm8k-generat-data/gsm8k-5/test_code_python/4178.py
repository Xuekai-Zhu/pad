def solution():
    acclimation_period = 1  # John takes 1 year to get acclimated back to school life
    basic_learning_period = 2  # John spends 2 years learning the basics of his field
    research_period = 2.75 * basic_learning_period  # John spends 75% more time on research than on basic learning
    dissertation_writing_period = acclimation_period / 2  # John spends half as long on writing his dissertation as his acclimation period

    # Calculate the total time John took to complete his PhD
    total_time = acclimation_period + basic_learning_period + research_period + dissertation_writing_period
    result = total_time
    return result

print(solution())