def solution():
    charlize_time = 20  # Charlize was 20 minutes late
    classmates_time = [charlize_time + 10, charlize_time + 10, charlize_time + 10, charlize_time + 10]  # Four classmates were each 10 minutes later than Charlize
    total_time = charlize_time + sum(classmates_time)  # Calculate the total time the five students were late
    result = total_time
    return result

print(solution())