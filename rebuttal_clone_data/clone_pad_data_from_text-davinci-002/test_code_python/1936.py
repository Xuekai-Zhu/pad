def solution():
    number_of_participants = 7
    pot_size = number_of_participants * 5
    first_place_prize = pot_size * 0.8
    second_and_third_prize = (pot_size - first_place_prize) / 2
    third_place_prize = second_and_third_prize / 2
    result = third_place_prize
    return result

print(solution())