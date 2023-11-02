def solution():
    # Calculate the total revenue from pumpkin sales
    pumpkin_revenue = 96

    # Calculate the number of people who bought pumpkins
    num_people = pumpkin_revenue / 3

    # Calculate the number of pumpkins left after carving
    num_leftover_pumpkins = 83 - num_people

    # Calculate the number of cans of pie filling
    num_cans = num_leftover_pumpkins // 3

    result = num_cans
    return result

print(solution())