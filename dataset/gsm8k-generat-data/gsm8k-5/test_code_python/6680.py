def solution():
    total_computers = 20  # John had to fix 20 computers
    unfixable = int(0.2 * total_computers)  # 20% of the computers are unfixable
    waiting_for_parts = int(0.4 * total_computers)  # 40% of the computers need to wait for spare parts

    # Calculate the number of computers that John was able to fix right away
    fixed_right_away = total_computers - unfixable - waiting_for_parts
    result = fixed_right_away
    return result

print(solution())