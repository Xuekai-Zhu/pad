def solution():
    doubling_rate = 2
    previous_number_of_patients = 26
    current_number_of_patients = previous_number_of_patients * doubling_rate
    one_in_four = 1/4
    patients_with_syndrome = current_number_of_patients * one_in_four
    result = patients_with_syndrome
    return result

print(solution())