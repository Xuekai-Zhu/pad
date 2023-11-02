def solution():
    Ticket_One = 150
    Ticket_Two = 150
    Ticket_Three = Ticket_One / 3
    Total_Cost = Ticket_One + Ticket_Two + Ticket_Three
    Money_Left = 500 - (Total_Cost / 2)
    result = Money_Left
    return result

print(solution())