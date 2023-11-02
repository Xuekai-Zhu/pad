def solution():
    is_hanuman_a_lifelong_celibate = True
    celibates_refrain_from_sexual_activity = True
    orgasms_only_occur_during_sexual_activity = True
    if is_hanuman_a_lifelong_celibate and celibates_refrain_from_sexual_activity and not orgasms_only_occur_during_sexual_activity:
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())