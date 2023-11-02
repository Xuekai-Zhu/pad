def solution():
    num_males_orchestra = 11
    num_females_orchestra = 12
    num_males_band = num_males_orchestra * 2
    num_females_band = num_females_orchestra * 2
    num_males_choir = 12
    num_females_choir = 17

    total_orchestra = num_males_orchestra + num_females_orchestra
    total_band = num_males_band + num_females_band
    total_choir = num_males_choir + num_females_choir

    total_musicians = total_orchestra + total_band + total_choir
    result = total_musicians
    return result

print(solution())