def solution():
    """A mailman has to deliver 48 pieces of junk mail. There are 8 houses on the block. 2 of the houses have white mailboxes and 3 have red mailboxes. How many pieces of junk mail will each of those houses get?"""
    total_mail = 48
    total_houses = 8
    white_mailboxes = 2
    red_mailboxes = 3

    # total number of houses without white or red mailboxes
    other_houses = total_houses - white_mailboxes - red_mailboxes

    # calculate number of mail pieces for each color mailbox
    white_mail = total_mail * (white_mailboxes / total_houses)
    red_mail = total_mail * (red_mailboxes / total_houses)
    other_mail = total_mail * (other_houses / total_houses)

    # calculate how many pieces each house will receive
    white_mail_per_house = white_mail / white_mailboxes
    red_mail_per_house = red_mail / red_mailboxes
    other_mail_per_house = other_mail / other_houses

    result = (white_mail_per_house, red_mail_per_house, other_mail_per_house)
    return result

print(solution())