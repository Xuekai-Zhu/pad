def solution():
    # Calculate the total distance driven
    total_distance = 400 + 200  # today's distance + tomorrow's distance

    # Calculate the total amount of gas consumed
    gas_consumed = total_distance * 4  # 4 gallons of gas per mile

    result = gas_consumed
    return result

print(solution())