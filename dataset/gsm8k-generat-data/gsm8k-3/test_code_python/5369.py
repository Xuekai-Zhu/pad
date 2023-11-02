def solution():
    """Matt has a peanut plantation that is 500 feet by 500 feet. 1 square foot of peanuts can make 50 grams of peanuts. If it takes 20 grams of peanuts to make 5 grams of peanut butter and 1 kg of peanut butter sells for $10 how much does he make from his plantation?"""
    # Define the size of the peanut plantation in square feet
    plantation_size = 500 * 500

    # Calculate the total weight of peanuts produced in the plantation
    total_peanut_weight = plantation_size * 50

    # Calculate the weight of peanut butter that can be made from the total weight of peanuts
    peanut_butter_weight = (total_peanut_weight / 20) * 5

    # Calculate the total revenue from selling the peanut butter
    revenue = (peanut_butter_weight / 1000) * 10

    # Display the total revenue
    result = revenue
    return result

print(solution())