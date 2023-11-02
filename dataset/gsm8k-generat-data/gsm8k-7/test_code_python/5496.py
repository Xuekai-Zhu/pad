def solution():
    current_total = 10  # starting with 10 people on the trolley
    current_total -= 3  # 3 people got off on the second stop

    # Twice as many people from the first stop got on at the second stop
    current_total += 2 * 10

    current_total -= 18  # 18 people got off on the third stop
    current_total += 2  # 2 people got on at the third stop

    result = current_total
    return result

print(solution())