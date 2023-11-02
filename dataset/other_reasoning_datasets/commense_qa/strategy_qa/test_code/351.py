def solution():
    bonanza_episodes = 431
    wwe_heat_episodes = 513
    bonanza_runtime = 49
    wwe_heat_runtime = 45
    bonanza_total_runtime = bonanza_episodes * bonanza_runtime
    wwe_heat_total_runtime = wwe_heat_episodes * wwe_heat_runtime
    if bonanza_total_runtime < wwe_heat_total_runtime:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())