def solution():
    # Define the total number of pieces of candy
    total_candy = 418
    
    # Define the number of pieces of candy Taquon and Mack had combined
    taquon_mack_candy = 171 * 2
    
    # Calculate the number of pieces of candy Jafari had
    jafari_candy = total_candy - taquon_mack_candy
    result = jafari_candy
    return result

print(solution())