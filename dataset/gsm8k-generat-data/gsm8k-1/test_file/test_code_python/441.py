Sorry, there seems to be a mistake in the previous answer. Here's the correct solution for the next question:

def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamie_last_name = "Grey"
    bobbie_last_name = jamie_last_name * 2
    bobbie_last_name = bobbie_last_name[:-2]
    samantha_last_name = bobbie_last_name[:-3]
    result = len(samantha_last_name)
    return result

Question: Michael is racing his horse and notices that for every mile the horse runs, he eats 1/2 a bail of hay. A bail of hay costs $3. If his horse runs for 30 minutes at 32MPH, and Michael has six 5 dollar bills, how much change does he have after he buys the hay?
Solution:
def solution():
    """Michael is racing his horse and notices that for every mile the horse runs, he eats 1/2 a bail of hay. A bail of hay costs $3. If his horse runs for 30 minutes at 32MPH, and Michael has six 5 dollar bills, how much change does he have after he buys the hay?"""
    horse_speed = 32 # miles per hour
    time = 0.5 # 30 minutes is half an hour
    distance = horse_speed * time
    hay_bails = distance / 2 # 1/2 bails of hay per mile
    hay_cost = hay_bails * 3
    money = 6 * 5 # six 5 dollar bills
    change = money - hay_cost
    result = change
    return result

print(solution())