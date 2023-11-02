def solution():
    day_1_alina = 120 - 20
    day_2_alina = day_1_alina * 2
    day_2_lucia = 120 / 3
    day_3_alina = day_1_alina
    day_3_lucia = day_2_lucia
    total_messages = day_1_alina + day_2_alina + day_3_alina + day_2_lucia + day_3_lucia
    result = total_messages
    return result

print(solution())