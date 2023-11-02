def solution():
    # Define the initial number of sausages
    sausages = 600

    # Calculate the number of sausages eaten on Monday
    sausages_eaten_on_monday = sausages * (2/5)

    # Calculate the number of sausages remaining after Monday
    remaining_sausages_after_monday = sausages - sausages_eaten_on_monday

    # Calculate the number of sausages eaten on Tuesday
    sausages_eaten_on_tuesday = remaining_sausages_after_monday * (1/2)

    # Calculate the number of sausages remaining after Tuesday
    remaining_sausages_after_tuesday = remaining_sausages_after_monday - sausages_eaten_on_tuesday

    # Calculate the number of sausages eaten on Friday
    sausages_eaten_on_friday = remaining_sausages_after_tuesday * (3/4)

    # Calculate the number of sausages remaining after Friday
    remaining_sausages_after_friday = remaining_sausages_after_tuesday - sausages_eaten_on_friday

    result = remaining_sausages_after_friday
    return result

print(solution())