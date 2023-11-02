def solution():
    # Calculate the total number of houses that will receive mail
    total_houses = 8

    # Calculate the number of houses with white mailboxes
    white_mailbox_houses = 2

    # Calculate the number of houses with red mailboxes
    red_mailbox_houses = 3

    # Calculate the total number of houses without a colored mailbox
    no_colored_mailbox_houses = total_houses - (white_mailbox_houses + red_mailbox_houses)

    # Calculate the total number of pieces of junk mail that will be delivered to houses without colored mailboxes
    no_colored_mailbox_mail = 48 / no_colored_mailbox_houses

    # Calculate the total number of pieces of junk mail that will be delivered to houses with white mailboxes
    white_mailbox_mail = 48 / white_mailbox_houses

    # Calculate the total number of pieces of junk mail that will be delivered to houses with red mailboxes
    red_mailbox_mail = 48 / red_mailbox_houses

    result = (no_colored_mailbox_mail, white_mailbox_mail, red_mailbox_mail)
    return result

print(solution())