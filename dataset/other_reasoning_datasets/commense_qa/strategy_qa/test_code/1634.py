def solution():
    one_thousand_and_one_nights_compiled = 1001
    islamic_golden_age_start = 800
    islamic_golden_age_end = 1258
    canterbury_tales_written = 1392
    
    if canterbury_tales_written < islamic_golden_age_start or canterbury_tales_written < one_thousand_and_one_nights_compiled:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())