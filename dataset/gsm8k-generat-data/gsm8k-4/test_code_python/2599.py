def solution():
    """Amy bought a 15-foot spool of string to cut up into wicks for making candles. If she cuts up the entire string into an equal number of 6-inch and 12-inch wicks, what is the total number of wicks she will have cut?"""
    # Define the length of the string in inches
    string_length_inches = 15 * 12
    
    # Define the length of each wick in inches
    wick1_length_inches = 6
    wick2_length_inches = 12
    
    # Calculate the total number of wicks that can be cut
    wick1_count = string_length_inches // wick1_length_inches
    wick2_count = string_length_inches // wick2_length_inches
    
    # Calculate the total number of wicks
    wick_count = wick1_count + wick2_count
    
    # return the result
    result = wick_count
    return result

print(solution())