def solution():
    """Matt has a peanut plantation that is 500 feet by 500 feet. 1 square foot of peanuts can make 50 grams of peanuts. If it takes 20 grams of peanuts to make 5 grams of peanut butter and 1 kg of peanut butter sells for $10 how much does he make from his plantation?"""
    # Define the size of the peanut plantation
    width = 500
    length = 500

    # Calculate the total area of the plantation
    area = width * length

    # Calculate the total weight of peanuts produced in grams
    weight = area * 50

    # Calculate the weight of peanut butter that can be made
    peanut_butter_weight = weight / 20 * 5

    # Calculate the total profit from selling peanut butter
    profit = peanut_butter_weight / 1000 * 10

    # Return the result
    result = profit
    return result

print(solution())