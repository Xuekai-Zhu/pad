def solution():
    wilson_vote = 41
    roosevelt_vote = 27
    taft_vote = 23
    debs_vote = 6
    total_vote = wilson_vote + roosevelt_vote + taft_vote + debs_vote
    if wilson_vote > (total_vote / 2):
        result = "yes"
    elif roosevelt_vote > (total_vote / 2):
        result = "yes"
    elif taft_vote > (total_vote / 2):
        result = "yes"
    elif debs_vote > (total_vote / 2):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())