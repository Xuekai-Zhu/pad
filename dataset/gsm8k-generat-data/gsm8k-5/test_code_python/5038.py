def solution(): 
    peanuts_in_jar = 148  # There were 148 peanuts in the jar
    brock_consumed = peanuts_in_jar / 4  # Brock ate one-fourth of the peanuts
    bonita_consumed = 29  # Bonita ate 29 peanuts

    # Calculate the number of peanuts left in the jar
    peanuts_left = peanuts_in_jar - brock_consumed - bonita_consumed
    
    result = peanuts_left
    return result

print(solution())