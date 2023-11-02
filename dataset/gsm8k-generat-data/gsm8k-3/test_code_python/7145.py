def solution():
    """Mark constructs a cube of pure gold.  The cube is 6 cm on each side.  The density of gold is 19 grams per cubic centimeter.  He buys the gold for $60 per gram.  He sells it for 1.5 times its gold value.  What was the profit?"""
    
    #Calculate the volume of the cube
    volume = 6**3

    #Calculate the mass of the cube
    mass = volume * 19

    #Calculate the cost of the gold
    cost = mass * 60

    #Calculate the selling price of the cube
    selling_price = cost * 1.5

    #Calculate the profit
    profit = selling_price - cost

    result = profit
    return result

print(solution())