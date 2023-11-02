def solution():
    initial_peanuts = 148  # number of peanuts in the jar initially
    brock_peanuts = (1/4) * initial_peanuts  # number of peanuts Brock ate
    remaining_peanuts = initial_peanuts - brock_peanuts - 29  # number of peanuts remaining after Bonita ate and Brock ate
    result = remaining_peanuts
    return result

print(solution())