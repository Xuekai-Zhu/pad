def solution():
    limbic_system_functions = ["detect fear", "control bodily functions", "perceive sensory information"]
    exorcist_ranking = 3
    if "detect fear" in limbic_system_functions and exorcist_ranking <= 3:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())