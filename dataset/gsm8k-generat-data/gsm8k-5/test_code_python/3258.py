def solution():
    total_sausages = 600  # Mr Castiel prepared 600 boar sausages

    # Sausages eaten on Monday
    sausages_monday = (2/5) * total_sausages

    # Remaining sausages after Monday
    remaining_sausages = total_sausages - sausages_monday

    # Sausages eaten on Tuesday
    sausages_tuesday = (1/2) * remaining_sausages

    # Remaining sausages after Tuesday
    remaining_sausages = remaining_sausages - sausages_tuesday

    # Sausages eaten on Friday
    sausages_friday = (3/4) * remaining_sausages

    # Total sausages left
    sausages_left = remaining_sausages - sausages_friday
    result = sausages_left
    return result

print(solution())