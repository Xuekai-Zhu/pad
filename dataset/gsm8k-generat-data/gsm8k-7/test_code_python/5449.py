def solution():
    total_junk_mail = 48
    num_houses = 8
    num_white_mailboxes = 2
    num_red_mailboxes = 3

    # Calculate the total number of houses that do not have white or red mailboxes
    num_other_houses = num_houses - num_white_mailboxes - num_red_mailboxes

    # Calculate the total number of pieces of junk mail to be delivered to the white mailbox houses
    white_mailbox_junk_mail = (total_junk_mail / num_houses) * num_white_mailboxes

    # Calculate the total number of pieces of junk mail to be delivered to the red mailbox houses
    red_mailbox_junk_mail = (total_junk_mail / num_houses) * num_red_mailboxes

    # Calculate the number of pieces of junk mail each white mailbox house will receive
    white_mailbox_per_house = white_mailbox_junk_mail / num_white_mailboxes

    # Calculate the number of pieces of junk mail each red mailbox house will receive
    red_mailbox_per_house = red_mailbox_junk_mail / num_red_mailboxes

    # Calculate the number of pieces of junk mail each of the remaining houses will receive
    other_houses_per_house = (total_junk_mail - white_mailbox_junk_mail - red_mailbox_junk_mail) / num_other_houses

    result = {"White Mailbox Houses": white_mailbox_per_house, "Red Mailbox Houses": red_mailbox_per_house,
              "Other Houses": other_houses_per_house}
    return result

print(solution())