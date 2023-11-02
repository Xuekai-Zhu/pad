def solution():
    # Find Shay's current age
    shay_age = 6 + 13  # Shay is 13 years older than Thomas

    # Find James' current age
    james_age = shay_age + 5  # James is 5 years older than Shay

    # Find how many years it will take Thomas to reach James' current age
    years_until_same_age = james_age - 6  # Thomas is currently 6 years old

    # Find James' age by that time
    james_future_age = james_age + years_until_same_age

    result = james_future_age
    return result

print(solution())