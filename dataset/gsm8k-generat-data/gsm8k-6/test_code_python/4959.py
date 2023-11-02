def solution():
    total_MC = 35  # total number of multiple-choice questions to write
    total_PS = 15  # total number of problem-solving questions to write
    written_MC = (2/5) * total_MC  # number of multiple-choice questions already written
    written_PS = (1/3) * total_PS  # number of problem-solving questions already written
    remaining_MC = total_MC - written_MC  # number of multiple-choice questions left to write
    remaining_PS = total_PS - written_PS  # number of problem-solving questions left to write
    total_remaining = remaining_MC + remaining_PS  # total number of questions left to write

    result = total_remaining
    return result

print(solution())