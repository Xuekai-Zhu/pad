def solution():
    # Define the number of pencils Ken gave to Manny
    pencils_manny = 10
    
    # Define the number of pencils Ken gave to Nilo
    pencils_nilo = pencils_manny + 10
    
    # Calculate the total number of pencils Ken gave away
    pencils_given = pencils_manny + pencils_nilo
    
    # Calculate the number of pencils Ken kept
    pencils_kept = 50 - pencils_given
    
    result = pencils_kept
    return result

print(solution())