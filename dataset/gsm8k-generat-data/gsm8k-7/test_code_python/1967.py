def solution():
    monday_hotdogs = 10
    additional_hotdogs = 2

    # Calculate the total number of hotdogs by Wednesday
    wednesday_hotdogs = monday_hotdogs + additional_hotdogs + (additional_hotdogs * 2)

    result = wednesday_hotdogs
    return result

print(solution())