def solution():
    """A pumpkin patch allows people to come pick pumpkins to carve in the fall every year. They charge $3 per person for a pumpkin. The remaining pumpkins get turned into cans of pie filling, 3 pumpkins to a can. They grew 83 pumpkins this year and made $96 selling pumpkins for carving. How many cans of pie filling will the pumpkin patch produce?"""
    # Define the price per pumpkin and the number of pumpkins grown
    PRICE_PER_PUMPKIN = 3
    NUM_PUMPKINS = 83

    # Calculate the total revenue from selling pumpkins for carving
    pumpkin_revenue = PRICE_PER_PUMPKIN * (NUM_PUMPKINS // 3)

    # Calculate the number of pumpkins left over for pie filling
    leftover_pumpkins = NUM_PUMPKINS % 3

    # Calculate the number of cans of pie filling
    num_cans = (NUM_PUMPKINS - leftover_pumpkins) // 3

    # Display the number of cans of pie filling
    result = num_cans
    return result

print(solution())