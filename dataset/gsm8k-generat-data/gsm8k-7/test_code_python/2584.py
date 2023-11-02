def solution():
    total_flyers = 200
    flyers_passed_out = 42 + 67 + 51   # flyers passed out by Ryan, Alyssa and Scott
    flyers_belinda_passed_out = total_flyers - flyers_passed_out

    # Calculate the percentage of flyers passed out by Belinda
    percentage_belinda_passed_out = (flyers_belinda_passed_out / total_flyers) * 100
    result = percentage_belinda_passed_out
    return result

print(solution())