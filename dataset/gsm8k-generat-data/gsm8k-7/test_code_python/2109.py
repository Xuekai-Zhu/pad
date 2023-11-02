def solution():
    num_volcanoes = 200

    # Calculate the number of volcanoes that erupted in the first two months
    erupted_in_2_months = int(num_volcanoes * 0.2)

    # Calculate the number of remaining volcanoes after the first two months
    remaining_volcanoes = num_volcanoes - erupted_in_2_months

    # Calculate the number of volcanoes that erupted by the half of the year
    erupted_by_half = int(remaining_volcanoes * 0.4)

    # Calculate the remaining number of volcanoes after the half of the year
    remaining_volcanoes = remaining_volcanoes - erupted_by_half

    # Calculate the number of volcanoes that erupted at the end of the year
    erupted_at_end = int(remaining_volcanoes * 0.5)

    # Calculate the final number of intact mountains
    intact_mountains = remaining_volcanoes - erupted_at_end
    result = intact_mountains
    return result

print(solution())