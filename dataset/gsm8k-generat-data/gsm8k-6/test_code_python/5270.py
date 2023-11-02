def solution():
    # Calculate the total amount of basil Cheryl can harvest
    total_basil = 16 * 8  # 16 cups of basil per week for 8 weeks

    # Calculate the number of cups of pesto Cheryl can make
    cups_of_pesto = total_basil // 4  # 4 cups of basil per 1 cup of pesto
    result = cups_of_pesto
    return result

print(solution())