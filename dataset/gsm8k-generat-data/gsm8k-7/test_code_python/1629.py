def solution():
    new_visitors_per_hour = 50
    hours_open_per_day = 8
    total_visitors_per_day = new_visitors_per_hour * hours_open_per_day

    # Calculate the number of visitors who go to the gorilla exhibit
    gorilla_visitors = total_visitors_per_day * 0.8
    result = gorilla_visitors
    return result

print(solution())