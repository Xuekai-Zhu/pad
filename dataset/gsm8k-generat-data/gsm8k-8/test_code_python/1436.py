def solution():
    # Define Charlie's instruments
    charlie_flutes = 1
    charlie_horns = 2
    charlie_harps = 1

    # Define Carli's instruments
    carli_flutes = 2 * charlie_flutes
    carli_horns = 0.5 * charlie_horns
    carli_harps = 0

    # Calculate the total number of instruments owned by both
    total_instruments = (charlie_flutes + carli_flutes +
                        charlie_horns + carli_horns + charlie_harps + carli_harps)
    result = total_instruments
    return result

print(solution())