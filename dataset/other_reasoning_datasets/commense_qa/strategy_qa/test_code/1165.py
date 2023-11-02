def solution():
    # Define if snoring is a sign of sleep apnea and if sleep apnea is a sign of good breathing while sleeping
    snoring_sign = False
    sleep_apnea_sign = False
    good_breathing_sign = not(snoring_sign) and not(sleep_apnea_sign)
    if good_breathing_sign:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())