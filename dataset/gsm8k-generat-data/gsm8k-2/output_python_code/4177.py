def solution():
    """John decides to go back to school to get his PhD.  He first takes 1 year of courses to get acclimated back to school life before starting his PhD. After that, he spends 2 years learning the basics of his field.  He then starts research, and he spends 75% more time on research than he did learning the basics.  He then spends half as long on writing his dissertation as his acclimation period.  How long did it take him to do everything?"""
    acclimation_period = 1
    basics_learning_period = 2
    research_period = 2.75 * basics_learning_period
    writing_period = 0.5 * acclimation_period
    total_time = acclimation_period + basics_learning_period + research_period + writing_period
    result = total_time
    return result

print(solution())