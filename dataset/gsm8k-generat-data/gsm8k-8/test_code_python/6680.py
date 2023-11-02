def solution():
    # Define the total number of computers
    total_computers = 20

    # Calculate the number of unfixable computers
    unfixable_computers = 0.2 * total_computers

    # Calculate the number of computers that need to wait for spare parts
    parts_computers = 0.4 * total_computers

    # Calculate the number of computers that John was able to fix right away
    fixed_computers = total_computers - unfixable_computers - parts_computers

    result = fixed_computers
    return result

print(solution())