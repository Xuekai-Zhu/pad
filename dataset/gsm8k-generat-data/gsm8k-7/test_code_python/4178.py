def solution():
    acclimation_period = 1
    basic_learning_period = 2
    research_period = 2.75 * basic_learning_period
    dissertation_writing_period = 0.5 * acclimation_period

    total_time = acclimation_period + basic_learning_period + research_period + dissertation_writing_period

    result = total_time
    return result

print(solution())