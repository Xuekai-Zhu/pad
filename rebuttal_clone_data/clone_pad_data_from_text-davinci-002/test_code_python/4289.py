def solution():
    total_miles = 10
    miles_slow = 2
    miles_fast = 4
    miles_home_slow = total_miles - miles_slow - miles_fast
    result = miles_slow + miles_home_slow
    return result

print(solution())