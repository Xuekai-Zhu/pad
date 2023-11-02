def solution():
    # Calculate the number of hamburgers sold by Frank so far
    hamburgers_sold = 4*2 + 2*2  # 2 customers purchased 4 hamburgers and another 2 customers purchased 2 hamburgers
    # Calculate how much money Frank has earned so far
    total_earned = hamburgers_sold * 5  # each hamburger is sold for $5
    # Calculate how many more hamburgers Frank needs to sell to make $50
    hamburgers_needed = (50 - total_earned) / 5  # $50 is the target revenue
    result = int(hamburgers_needed)  # result should be a whole number
    return result

print(solution())