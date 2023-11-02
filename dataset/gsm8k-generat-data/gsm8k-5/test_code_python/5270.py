def solution():
    basil_per_pesto = 4  # It takes 4 cups of basil to make 1 cup of pesto
    weekly_basil_harvest = 16  # Cheryl harvests 16 cups of basil from her farm every week
    weeks = 8  # Cheryl can harvest basil for 8 weeks

    # Calculate the total amount of basil Cheryl will have
    total_basil = weekly_basil_harvest * weeks

    # Calculate the total amount of pesto Cheryl can make
    total_pesto = total_basil // basil_per_pesto

    result = total_pesto
    return result

print(solution())