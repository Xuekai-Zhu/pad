def solution():
     """Ayla has a customer care job whose primary role is to hear complaints from customers and advise them on the best way to solve their problems. She talks with each customer for a limited amount of time, and each phone call is charged five cents per minute. If each call lasts 1 hour, what's the phone bill at the end of the month if she manages to talk to 50 customers a week?"""
     customers_per_week = 50
     minutes_per_call = 60
     cost_per_minute = 0.05
     bill = customers_per_week * minutes_per_call * cost_per_minute
     result = bill
     return result

print(solution())