def solution():
    total_ceilings = 28  # Michelangelo has 28 ceilings to paint
    ceilings_painted_week1 = 12  # Michelangelo paints 12 ceilings in the first week
    ceilings_painted_week2 = ceilings_painted_week1 / 4  # Michelangelo paints 1/4 as many ceilings in the second week
    
    # Calculate the total number of ceilings painted after two weeks
    total_ceilings_painted = ceilings_painted_week1 + ceilings_painted_week2
    
    # Calculate the number of ceilings remaining to be painted after two weeks
    remaining_ceilings = total_ceilings - total_ceilings_painted
    result = remaining_ceilings
    return result

print(solution())