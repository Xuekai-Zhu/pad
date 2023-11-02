def solution():
    american_flag_stripes = 13
    goofys_voice_actors = 6
    bugs_bunnys_voice_actors = 7
    total_voice_actors = goofys_voice_actors + bugs_bunnys_voice_actors
    if total_voice_actors <= american_flag_stripes:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())