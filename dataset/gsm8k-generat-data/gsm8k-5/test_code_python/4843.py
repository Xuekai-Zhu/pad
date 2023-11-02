def solution():
    soccer_days = 3  # Josh has soccer practice for 3 days
    soccer_time = 2  # Josh has soccer practice for 2 hours each day
    band_days = 2  # Josh has band practice for 2 days
    band_time = 1.5  # Josh has band practice for 1.5 hours each day

    # Calculate the total time Josh spends on extracurricular activities from Monday to Friday
    total_time = (soccer_days * soccer_time) + (band_days * band_time)

    result = total_time
    return result

print(solution())