def solution():
    kane_record = 53.76
    benoit_record = 60.0
    any_murderers_outlasted = False
    if benoit_record > kane_record:
        any_murderers_outlasted = True
    if any_murderers_outlasted:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())