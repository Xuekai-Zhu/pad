def solution():
    # Define variables
    total_apples = 80
    ali_apples = 4
    sara_apples = 1

    # Calculate total number of Sara's apples
    sara_apples_total = total_apples / (ali_apples + sara_apples)

    # Calculate number of Ali's apples
    ali_apples_total = sara_apples_total * ali_apples

    result = sara_apples_total
    return result

print(solution())