def solution():
    zander_stickers = 100  # Zander collected 100 stickers
    andrew_stickers = zander_stickers / 5  # Andrew received 1/5 of Zander's stickers
    remaining_stickers = zander_stickers - andrew_stickers  # Calculate the remaining stickers after Andrew has received his share
    bill_stickers = 3/10 * remaining_stickers  # Bill received 3/10 of the remaining stickers
    total_given = andrew_stickers + bill_stickers  # Calculate the total stickers given away by Zander
    andrew_gave = total_given / 2  # Andrew gave half of the total stickers given away to his friends
    result = andrew_gave
    return result

print(solution())