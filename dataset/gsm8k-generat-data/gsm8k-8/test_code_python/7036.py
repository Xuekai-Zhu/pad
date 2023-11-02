def solution():
    # Calculate Melissa's number of dresses
    melissa_dresses = Emily_dresses / 2
    
    # Calculate Debora's number of dresses
    debora_dresses = melissa_dresses + 12
    
    # Calculate the total number of dresses
    total_dresses = Emily_dresses + melissa_dresses + debora_dresses
    
    result = total_dresses
    return result

print(solution())