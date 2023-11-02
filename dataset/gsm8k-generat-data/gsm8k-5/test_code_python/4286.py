def solution():
    initial_blondes = 30  # There were 30 blonde-haired girls in the choir initially
    total_students = 80  # The choir has a total of 80 girls
    new_blondes = 10  # The teacher added 10 more blonde-haired girls

    # Calculate the number of black-haired girls in the choir
    initial_black = total_students - initial_blondes  # The initial number of black-haired girls
    final_blondes = initial_blondes + new_blondes  # The final number of blonde-haired girls
    final_black = total_students - final_blondes  # The final number of black-haired girls

    result = final_black
    return result

print(solution())