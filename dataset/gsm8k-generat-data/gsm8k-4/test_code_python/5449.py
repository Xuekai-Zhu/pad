def solution():
    """A mailman has to deliver 48 pieces of junk mail. There are 8 houses on the block. 2 of the houses have white mailboxes and 3 have red mailboxes. How many pieces of junk mail will each of those houses get?"""
    # Define the total number of houses and the number of houses with each color mailbox
    total_houses = 8
    white_mailboxes = 2
    red_mailboxes = 3

    # Calculate the total number of houses with mailboxes
    mailbox_houses = white_mailboxes + red_mailboxes

    # Calculate the total number of pieces of mail per house
    total_mail_per_house = 48 / total_houses

    # Calculate the number of pieces of mail each house with a white mailbox will receive
    white_mail_per_house = total_mail_per_house * (white_mailboxes / mailbox_houses)

    # Calculate the number of pieces of mail each house with a red mailbox will receive
    red_mail_per_house = total_mail_per_house * (red_mailboxes / mailbox_houses)

    # return the result
    result = round(red_mail_per_house)
    return result

print(solution())