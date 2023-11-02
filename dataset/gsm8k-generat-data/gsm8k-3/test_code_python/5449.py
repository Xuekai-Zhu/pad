def solution():
    """A mailman has to deliver 48 pieces of junk mail.  There are 8 houses on the block.  2 of the houses have white mailboxes and 3 have red mailboxes.  How many pieces of junk mail will each of those houses get?"""
    # Define the number of houses with white and red mailboxes
    white_mailboxes = 2
    red_mailboxes = 3

    # Calculate the total number of houses
    total_houses = 8

    # Calculate the number of houses with other color mailboxes
    other_mailboxes = total_houses - white_mailboxes - red_mailboxes

    # Calculate the total number of junk mail pieces per house
    total_junk_mail = 48
    junk_mail_per_house = total_junk_mail / total_houses

    # Calculate the number of junk mail pieces for houses with white mailboxes
    white_junk_mail = junk_mail_per_house * white_mailboxes

    # Calculate the number of junk mail pieces for houses with red mailboxes
    red_junk_mail = junk_mail_per_house * red_mailboxes

    # Calculate the number of junk mail pieces for houses with other color mailboxes
    other_junk_mail = junk_mail_per_house * other_mailboxes

    # Display the number of junk mail pieces per house for white, red, and other color mailboxes
    result = (white_junk_mail, red_junk_mail, other_junk_mail)
    return result

print(solution())