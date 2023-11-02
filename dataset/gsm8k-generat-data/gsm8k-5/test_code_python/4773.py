def solution():
    initial_doctors = 11  # There are 11 doctors initially
    initial_nurses = 18  # There are 18 nurses initially
    quitting_doctors = 5  # 5 doctors have quit
    quitting_nurses = 2  # 2 nurses have quit

    # Calculate the number of doctors and nurses left
    remaining_doctors = initial_doctors - quitting_doctors
    remaining_nurses = initial_nurses - quitting_nurses
    result = (remaining_doctors, remaining_nurses)
    return result

print(solution())