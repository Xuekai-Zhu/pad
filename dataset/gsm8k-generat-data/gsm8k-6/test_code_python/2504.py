def solution():
    # Calculate the number of wipes that Elsie started with
    refill_count = (60 - 20) / 10  # number of times Elsie refilled the container throughout the day
    start_count = 20 + (refill_count * 10)  # initial number of wipes plus refills
    result = start_count
    return result

print(solution())