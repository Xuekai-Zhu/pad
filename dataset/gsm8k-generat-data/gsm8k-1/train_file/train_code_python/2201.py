def solution():
    """In one of the building blocks at Oakland High there are 5 classes. Each class uses 2 whiteboards each and each whiteboard needs about 20ml of ink for a day's use. If ink costs 50 cents per ml, how much (in dollars) would it cost to use the boards for one day?"""
    num_classes = 5
    whiteboards_per_class = 2
    ink_per_whiteboard = 20 # in ml
    ink_price_per_ml = 0.5 # in dollars
    total_ink = num_classes * whiteboards_per_class * ink_per_whiteboard
    total_cost = total_ink * ink_price_per_ml
    result = total_cost
    return result

print(solution())