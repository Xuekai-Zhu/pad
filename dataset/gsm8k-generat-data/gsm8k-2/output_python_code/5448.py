def solution():
    """A mailman has to deliver 48 pieces of junk mail. There are 8 houses on the block. 2 of the houses have white mailboxes and 3 have red mailboxes. How many pieces of junk mail will each of those houses get?"""
    white_mailboxes = 2
    red_mailboxes = 3
    total_houses = 8
    total_mailboxes = white_mailboxes + red_mailboxes
    remaining_houses = total_houses - total_mailboxes
    junk_mail_per_red = 48 / red_mailboxes
    junk_mail_per_white = 48 / white_mailboxes
    junk_mail_per_remaining = 48 / remaining_houses
    result = (junk_mail_per_red * red_mailboxes) + (junk_mail_per_white * white_mailboxes)
    return result

print(solution())