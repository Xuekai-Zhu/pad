def solution():
    """Bill milked his cow and got 16 gallons of milk. He turned 1/4 into sour cream, 1/4 into butter, and kept the rest as whole milk. 
    It takes 4 gallons of milk to make one gallon of butter and 2 gallons of milk to make 1 gallon of sour cream. 
    If Bill sells butter for $5/gallon, sour cream for $6/gallon, and whole milk for $3/gallon, how much money does he make?"""
    # Define the total amount of milk and the amounts turned into sour cream and butter
    total_milk = 16
    sour_cream = total_milk * 0.25 * 0.5   # 1/4 of the milk turned into sour cream, and it takes 2 gallons of milk to make 1 gallon of sour cream
    butter = total_milk * 0.25 * 0.25     # 1/4 of the milk turned into butter, and it takes 4 gallons of milk to make 1 gallon of butter
    
    # Calculate the amount of whole milk remaining
    whole_milk = total_milk - sour_cream - butter
    
    # Calculate the earnings from selling sour cream, butter, and whole milk
    sour_cream_earnings = sour_cream * 6
    butter_earnings = butter * 5
    whole_milk_earnings = whole_milk * 3
    
    # Calculate the total earnings
    total_earnings = sour_cream_earnings + butter_earnings + whole_milk_earnings
    
    # Return the result
    result = total_earnings
    return result

print(solution())