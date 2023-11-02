def solution():
    # Calculate the total water flow per minute
    total_flow = 2*2 + 2*3  # Two hoses each delivering 2 gallons/min and two hoses each delivering 3 gallons/min.
    
    # Calculate the total time needed to fill 15000 gallons of water
    # 1 gallon = 0.133681 cubic feet
    # Volume of the 24-foot round pool = pi * (12^2) = 452.39 cubic feet
    # Therefore, 15000 gallons = 2003.215 cubic feet
    total_time = (2003.215 / total_flow) * 60   # Converted minutes to hours by multiplying by 60
    
    result = total_time
    return result

print(solution())