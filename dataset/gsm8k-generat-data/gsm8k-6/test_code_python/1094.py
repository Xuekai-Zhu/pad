def solution():
    # Calculate the total amount of liquid in the jug
    total_liquid = 16  # initial amount of water added
    total_liquid -= 4  # amount of water that evaporated
    total_liquid *= 4  # quadruple the amount of water in the jug

    # Calculate the amount of koolaid powder in the jug
    koolaid_powder = 2  # initial amount of koolaid powder added

    # Calculate the percentage of the liquid in the jug that is koolaid powder
    percent_koolaid = (koolaid_powder / total_liquid) * 100
    result = percent_koolaid
    return result

print(solution())