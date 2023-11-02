def solution():
    # Calculate the number of boar sausages remaining after Monday
    remaining_sausages = 600 * (3/5)
    
    # Calculate the number of sausages eaten on Tuesday
    sausages_on_tuesday = remaining_sausages / 2
    
    # Calculate the number of sausages remaining for Friday
    remaining_for_friday = remaining_sausages - sausages_on_tuesday
    
    # Calculate the number of sausages eaten on Friday
    eaten_on_friday = remaining_for_friday * (3/4)
    
    # Calculate the number of sausages remaining after Friday
    remaining_sausages = remaining_for_friday - eaten_on_friday
    
    result = remaining_sausages
    return result

print(solution())