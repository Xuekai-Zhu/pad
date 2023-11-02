def solution():
    junk_mail = 48
    houses = 8
    white_mailboxes = 2
    red_mailboxes = 3
    pieces_per_house = junk_mail / houses
    pieces_per_white_mailbox = pieces_per_house / white_mailboxes
    pieces_per_red_mailbox = pieces_per_house / red_mailboxes
    result = [pieces_per_house, pieces_per_white_mailbox, pieces_per_red_mailbox]
    return result

print(solution())