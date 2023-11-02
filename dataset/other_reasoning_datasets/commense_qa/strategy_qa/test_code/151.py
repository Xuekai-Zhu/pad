def solution():
    supports_police = True
    opposes_violence = True
    # Check if members of Blue Lives Matter would support every element of Grand Theft Auto III
    if supports_police and opposes_violence:
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())