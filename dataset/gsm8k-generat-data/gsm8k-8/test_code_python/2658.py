def solution():
    # Define the total number of stickers collected
    zander_stickers = 100

    # Calculate the number of stickers Andrew received
    andrew_stickers = zander_stickers / 5

    # Calculate the number of stickers remaining after Andrew received his share
    remaining_stickers = zander_stickers - andrew_stickers

    # Calculate the number of stickers Bill received
    bill_stickers = remaining_stickers * 3 / 10

    # Calculate the total number of stickers given to Andrew's friends
    friends_stickers = andrew_stickers + bill_stickers

    result = friends_stickers
    return result

print(solution())