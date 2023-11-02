def solution():
    total_computers = 20
    unfixable_computers = total_computers * 0.2
    wait_computers = total_computers * 0.4

    # Calculate the number of computers that can be fixed right away
    fixed_computers = total_computers - unfixable_computers - wait_computers

    result = fixed_computers
    return result

print(solution())