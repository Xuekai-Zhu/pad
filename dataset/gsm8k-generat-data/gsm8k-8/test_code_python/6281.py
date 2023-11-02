def solution():
    # Define Bill's eel length
    bill_eel_length = x

    # Calculate Jenna's eel length
    jenna_eel_length = bill_eel_length * (1/3)

    # Calculate the total length
    total_length = bill_eel_length + jenna_eel_length

    # Solve for bill_eel_length using the given total length equation
    bill_eel_length = total_length / (1 + 1/3)

    # Calculate Jenna's eel length again with the solved bill_eel_length
    jenna_eel_length = bill_eel_length * (1/3)

    result = jenna_eel_length
    return result

print(solution())