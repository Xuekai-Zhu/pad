def solution():
    """Bill milked his cow and got 16 gallons of milk. He turned 1/4 into sour cream, 1/4 into butter, and kept the rest as whole milk. It takes 4 gallons of milk to make one gallon of butter and 2 gallons of milk to make 1 gallon of sour cream. If Bill sells butter for $5/gallon, sour cream for $6/gallon, and whole milk for $3/gallon, how much money does he make?"""
    # Define the amount of milk that goes into each product
    sour_cream_ratio = 0.25
    butter_ratio = 0.25
    whole_milk_ratio = 0.5

    # Calculate the amount of milk used to make sour cream and butter
    milk_for_sour_cream = sour_cream_ratio * 16
    milk_for_butter = butter_ratio * 16

    # Calculate the amount of sour cream and butter produced
    sour_cream = milk_for_sour_cream / 2
    butter = milk_for_butter / 4

    # Calculate the amount of whole milk remaining
    whole_milk = whole_milk_ratio * 16

    # Calculate the total earnings from selling the products
    earnings = (sour_cream * 6) + (butter * 5) + (whole_milk * 3)

    # Display the total earnings
    result = earnings
    return result

print(solution())