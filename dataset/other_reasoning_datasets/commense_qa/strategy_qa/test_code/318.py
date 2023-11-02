def solution():
    bing_has_rewards_program = True
    google_has_rewards_program = False
    duckduckgo_has_rewards_program = False
    if bing_has_rewards_program and not google_has_rewards_program and not duckduckgo_has_rewards_program:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())