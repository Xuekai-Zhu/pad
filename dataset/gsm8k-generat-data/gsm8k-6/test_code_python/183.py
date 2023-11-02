def solution():
    # Calculate the number of birds left after a week
    chickens_left = 300 - (20 * 7)  # 20 chickens lost per day for 7 days
    turkeys_left = 200 - (8 * 7)  # 8 turkeys lost per day for 7 days
    guinea_fowls_left = 80 - (5 * 7)  # 5 guinea fowls lost per day for 7 days
    total_birds_left = chickens_left + turkeys_left + guinea_fowls_left
    result = total_birds_left
    return result

print(solution())