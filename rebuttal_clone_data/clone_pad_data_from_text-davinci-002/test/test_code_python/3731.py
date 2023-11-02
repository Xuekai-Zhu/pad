def solution():
    minutes_per_call = 30
    call_charge = 0.05
    calls_per_week = 1
    weeks_per_year = 52
    total_calls = calls_per_week * weeks_per_year
    total_minutes = total_calls * minutes_per_call
    total_charge = total_minutes * call_charge
    result = total_charge
    return result

print(solution())