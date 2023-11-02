def solution():
    charlize_time = 20  # Charlize was 20 minutes late
    late_times = [charlize_time + 10, charlize_time + 10, charlize_time + 10, charlize_time + 10]  # 4 classmates were each 10 minutes late
    total_late_time = charlize_time + sum(late_times)  # sum of Charlize's late time and her classmates'
    result = total_late_time
    return result

print(solution())