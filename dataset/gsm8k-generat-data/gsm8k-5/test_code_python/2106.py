def solution():
    total_time = 7.5 * 12  # 7.5 years is equal to 90 months
    emilio_time = total_time * 2 / 3  # Felipe finished in half the time of Emilio, so Emilio took 2/3 of the total time
    felipe_time = total_time - emilio_time  # Felipe's time is the remaining time

    # Calculate the number of months it took Felipe to build his house
    months_felipe = felipe_time
    result = months_felipe
    return result

print(solution())