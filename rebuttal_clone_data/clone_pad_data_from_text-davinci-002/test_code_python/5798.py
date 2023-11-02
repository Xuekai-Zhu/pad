def solution():
    total_apples = 85
    bruised_apples = total_apples * 2/5
    wormy_apples = total_apples * 1/5
    unbruised_apples = total_apples - (bruised_apples + wormy_apples)
    result = unbruised_apples
    return result

print(solution())