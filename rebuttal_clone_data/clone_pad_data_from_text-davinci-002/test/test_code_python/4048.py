def solution():
    days_per_week = 7
    julien_meters = 50
    sarah_meters = julien_meters * 2
    jamir_meters = sarah_meters + 20
    total_meters = julien_meters + sarah_meters + jamir_meters
    result = total_meters * days_per_week
    return result

print(solution())