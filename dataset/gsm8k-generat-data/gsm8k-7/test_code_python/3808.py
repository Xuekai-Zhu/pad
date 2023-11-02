def solution():
    num_flutes = 20
    num_clarinets = 30
    num_trumpets = 60
    num_pianists = 20  # Assuming this means 20 students who play the piano tried out

    flute_acceptance_rate = 0.8
    clarinet_acceptance_rate = 0.5
    trumpet_acceptance_rate = 0.33333333333  # 1/3 as a decimal
    pianist_acceptance_rate = 0.1

    # Calculate the number of students who got into the band for each instrument
    num_flutes_in = num_flutes * flute_acceptance_rate
    num_clarinets_in = num_clarinets * clarinet_acceptance_rate
    num_trumpets_in = num_trumpets * trumpet_acceptance_rate
    num_pianists_in = num_pianists * pianist_acceptance_rate

    # Calculate the total number of students in the band
    total_students = num_flutes_in + num_clarinets_in + num_trumpets_in + num_pianists_in
    result = total_students
    return result

print(solution())