def solution():
    """A pumpkin patch allows people to come pick pumpkins to carve in the fall every year. They charge $3 per person for a pumpkin. The remaining pumpkins get turned into cans of pie filling, 3 pumpkins to a can. They grew 83 pumpkins this year and made $96 selling pumpkins for carving. How many cans of pie filling will the pumpkin patch produce?"""
    # Define the number of pumpkins grown and the revenue from pumpkin sales
    pumpkins_grown = 83
    pumpkin_revenue = 96

    # Calculate the number of pumpkins sold for carving
    pumpkins_carved = pumpkin_revenue / 3

    # Calculate the number of pumpkins left for pie filling
    pumpkins_pie = pumpkins_grown - pumpkins_carved

    # Calculate the number of cans of pie filling
    cans_pie = pumpkins_pie // 3

    # return the result
    result = cans_pie
    return result

print(solution())