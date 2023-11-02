def solution():
    # Define whether overfeeding Lactobacillus is unwise for people without dental insurance
    overfeeding_lactobacillus = True
    no_dental_insurance = True
    if overfeeding_lactobacillus and no_dental_insurance:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())