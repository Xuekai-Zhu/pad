def solution():
    """Barry, Thomas and Emmanuel are to share a jar of 200 jelly beans. If Thomas takes 10%, and Barry and Emmanuel are to share the remainder in the ratio 4:5 respectively, how many jelly beans will Emmanuel get?"""
    # Define the total number of jelly beans 
    total_jelly_beans = 200
    
    # Calculate the number of jelly beans taken by Thomas
    thomas_jelly_beans = total_jelly_beans * 0.1
    
    # Calculate the remaining jelly beans 
    remaining_jelly_beans = total_jelly_beans - thomas_jelly_beans
    
    # Calculate the total ratio for Barry and Emmanuel 
    total_ratio = 4 + 5
    
    # Calculate the share ratio for Emmanuel 
    emmanuel_ratio = 5 / total_ratio
    
    # Calculate the share of jelly beans for Emmanuel 
    emmanuel_jelly_beans = remaining_jelly_beans * emmanuel_ratio
    
    # Round the result to the nearest integer
    result = round(emmanuel_jelly_beans)
    return result

print(solution())