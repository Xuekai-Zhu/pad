def solution():
    carpenters = 8  # 8 carpenters can make 50 chairs in 10 days
    chairs = 50  # 8 carpenters can make 50 chairs in 10 days
    days = 10  # 8 carpenters can make 50 chairs in 10 days

    # Calculate how many carpenters are needed to make 75 chairs in 10 days
    required_carpenters = (75 * carpenters * days) / chairs
    result = required_carpenters
    return result

print(solution())