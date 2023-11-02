def solution():
    # Define the sodium limit for someone with heart failure and the sodium level in Ramen
    heart_failure_sodium_limit = 1500 # milligrams per day
    ramen_sodium_level = 1900 # milligrams per packet
    # Check if the Ramen sodium level exceeds the heart failure sodium limit
    if ramen_sodium_level > heart_failure_sodium_limit:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())