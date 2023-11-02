def solution():
    swan_lake_runtime = 145 # minutes
    min_bypass_surgery_time = 180 # minutes
    max_bypass_surgery_time = 360 # minutes
    if max_bypass_surgery_time < swan_lake_runtime:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())