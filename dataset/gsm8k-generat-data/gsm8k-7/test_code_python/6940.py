def solution():
    program_length = 30 # in minutes
    num_programs = 6

    # Calculate the total length of one program with commercials
    total_program_length = program_length / 0.75

    # Calculate the total length of all programs with commercials
    total_length = total_program_length * num_programs

    # Calculate the total time spent on commercials
    total_commercial_time = (program_length * 0.25) * num_programs

    result = total_commercial_time
    return result

print(solution())