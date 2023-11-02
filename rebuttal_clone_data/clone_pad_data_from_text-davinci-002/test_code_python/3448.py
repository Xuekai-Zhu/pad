def solution():
     towels_owned = 18
     towels_used_per_day = 2
     days_per_week = 7
     towels_washed_per_week = towels_owned / towels_used_per_day
     towels_available = towels_washed_per_week * days_per_week
     days_missed = 1
     towels_used_in_a_week = towels_used_per_day * days_per_week
     towels_remaining = towels_available - towels_used_in_a_week
     towels_needed = towels_used_in_a_week - towels_remaining
     result = towels_needed
     return result

print(solution())