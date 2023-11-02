def solution():
    monday_sites = 5
    monday_birds = 7
    monday_avg = monday_birds / monday_sites
    tuesday_sites = 5
    tuesday_birds = 5
    tuesday_avg = tuesday_birds / tuesday_sites
    wednesday_sites = 10
    wednesday_birds = 8
    wednesday_avg = wednesday_birds / wednesday_sites
    avg_across_days = (monday_avg + tuesday_avg + wednesday_avg) / 3
    result = avg_across_days
    return result

print(solution())