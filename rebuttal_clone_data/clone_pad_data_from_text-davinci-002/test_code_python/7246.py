def solution():
    pastor_paul_prays_per_day = 20
    pastor_bruce_prays_per_day = pastor_paul_prays_per_day / 2
    pastor_paul_sunday_prayer = pastor_paul_prays_per_day * 2
    pastor_bruce_sunday_prayer = pastor_bruce_prays_per_day * 2
    pastor_paul_total_prayer = pastor_paul_prays_per_day * 6 + pastor_paul_sunday_prayer
    pastor_bruce_total_prayer = pastor_bruce_prays_per_day * 6 + pastor_bruce_sunday_prayer
    prayers_prayed_by_paul = pastor_paul_total_prayer - pastor_bruce_total_prayer
    result = prayers_prayed_by_paul
    return result

print(solution())