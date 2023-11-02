def solution():
    matilda_chocolates = 20  # Matilda started with 20 chocolates
    total_people = 6  # Matilda, her 4 sisters, and her father
    initial_chocolates_per_person = matilda_chocolates / total_people  # They shared the chocolates evenly
    chocolates_gone_to_father = initial_chocolates_per_person * 4  # Each person gave up half of their chocolates
    father_chocolates = chocolates_gone_to_father + initial_chocolates_per_person  # Father received chocolates from others and himself
    father_chocolates -= 2  # Father ate 2 chocolates
    father_chocolates -= 3  # Father gave 3 chocolates to mother

    result = father_chocolates
    return result

print(solution())