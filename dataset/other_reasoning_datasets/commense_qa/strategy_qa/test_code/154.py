def solution():
    perfect_operation_record = False
    united_crash_incidents = 30
    if united_crash_incidents == 0:
        perfect_operation_record = True
    if perfect_operation_record:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())