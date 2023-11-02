def solution():
    walter_fell = 8  # Walter fell from the eighth platform
    additional_falls = 3  # Walter fell for an additional 3 times the depth he fell past David
    david_height = (walter_fell * 4) - (additional_falls * 4)  # David's height is the height at which Walter fell past David
    david_platform = david_height / 4 + 1  # Each platform is 4 meters high, and David was on a platform higher than the one Walter fell past
    result = david_platform
    return result

print(solution())