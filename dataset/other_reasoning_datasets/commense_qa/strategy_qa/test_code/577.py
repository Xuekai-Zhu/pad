def solution():
    # Define the relevant facts
    bool_algebra = True
    machine_language = True
    computer_programming = True
    # Check if a computer can be programmed entirely in Boolean algebra
    if bool_algebra and machine_language and computer_programming:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())