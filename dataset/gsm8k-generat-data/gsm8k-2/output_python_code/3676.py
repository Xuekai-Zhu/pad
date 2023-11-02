def solution():
    """A pumpkin patch allows people to come pick pumpkins to carve in the fall every year. They charge $3 per person for a pumpkin. The remaining pumpkins get turned into cans of pie filling, 3 pumpkins to a can. They grew 83 pumpkins this year and made $96 selling pumpkins for carving. How many cans of pie filling will the pumpkin patch produce?"""
    grown_pumpkins = 83
    carving_pumpkins_revenue = 96
    carving_pumpkins_sold = carving_pumpkins_revenue // 3
    total_pumpkins_sold = carving_pumpkins_sold + grown_pumpkins
    pie_filling_cans = (grown_pumpkins - carving_pumpkins_sold) // 3
    result = pie_filling_cans
    return result

print(solution())