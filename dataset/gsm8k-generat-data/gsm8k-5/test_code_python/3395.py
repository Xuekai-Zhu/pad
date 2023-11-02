def solution():
    canada_size = 1.5  # Canada is 1.5 times bigger than the United States
    russia_size = canada_size * 1.33  # Russia is 1/3 bigger than Canada
    us_size = 1  # Let the size of the United States be 1

    # Calculate how many times bigger Russia is than the United States
    russia_to_us_ratio = russia_size / us_size
    result = russia_to_us_ratio
    return result

print(solution())