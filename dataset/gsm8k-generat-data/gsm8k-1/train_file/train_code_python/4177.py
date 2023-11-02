def solution():
    """John decides to go back to school to get his PhD. He first takes 1 year of courses to get acclimated back to school life before starting his PhD. After that, he spends 2 years learning the basics of his field. He then starts research, and he spends 75% more time on research than he did learning the basics. He then spends half as long on writing his dissertation as his acclimation period. How long did it take him to do everything?"""
    acclimation_period = 1
    basics_period = 2
    research_period = basics_period * 1.75
    dissertation_period = acclimation_period / 2
    total_time = acclimation_period + basics_period + research_period + dissertation_period
    result = total_time
    return result

print(solution())