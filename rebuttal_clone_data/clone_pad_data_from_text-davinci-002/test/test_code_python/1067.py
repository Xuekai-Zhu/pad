def solution():
    time_frame = 4
    trevor_spending = 80
    reed_spending = trevor_spending - 20
    quinn_spending = reed_spending / 2
    total_spending = (trevor_spending * time_frame) + (reed_spending * time_frame) + (quinn_spending * time_frame)
    result = total_spending
    return result

print(solution())