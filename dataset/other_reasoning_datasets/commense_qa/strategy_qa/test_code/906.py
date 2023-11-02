def solution():
    hobbit_words = 95356
    hobbit_reading_time_berg = hobbit_words / 25000
    hobbit_reading_time_calderon = hobbit_words / 80000
    if hobbit_reading_time_calderon < 4:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())