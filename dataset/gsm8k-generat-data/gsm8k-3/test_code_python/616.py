def solution():
    """Kris is blowing up balloons for her sister’s party. 
    She has 30 minutes to blow up as many balloons as possible 
    and decides to enlist her brother’s help to increase the number of balloons. 
    Kris can blow up a total of 2 balloon per minute, 
    and her brother works twice as fast. After 15 minutes, 
    her brother doubles his speed and works at this new speed for the remaining 15 minutes. 
    After the 30 minutes, how many balloons, in total, did Kris and her brother blow up?"""
    
    # Calculate Kris's initial rate of balloon blowing
    kriss_rate = 2  # balloons per minute
    
    # Calculate Kris's total balloons after 30 minutes
    kriss_balloons_15 = kriss_rate * 15  # balloons blown by Kris in the first 15 minutes
    kriss_balloons_30 = kriss_rate * 30  # balloons blown by Kris in the entire 30 minutes
    
    # Calculate Kris's brother's rate of balloon blowing
    brothers_rate = kriss_rate * 2  # balloons per minute
    
    # Calculate Kris's brother's total balloons after 30 minutes
    brothers_balloons_15 = brothers_rate * 15  # balloons blown by the brother in the second 15 minutes
    brothers_balloons_30 = (brothers_rate * 15) + (kriss_rate * 15)  # balloons blown by the brother in the second 15 minutes and Kris in the whole 30 minutes
    
    # Calculate the total number of balloons blown by Kris and her brother in 30 minutes
    total_balloons = kriss_balloons_30 + brothers_balloons_30
    
    result = total_balloons
    return result

print(solution())