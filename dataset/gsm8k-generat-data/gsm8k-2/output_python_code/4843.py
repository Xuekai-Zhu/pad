def solution():
    """After trick-or-treating, Brent dumped his candy on the table. He had received 5 Kit-Kat bars, three times that amount in Hershey kisses, 8 boxes of Nerds, and 11 lollipops. He also had 10 Baby Ruths and half that amount in Reese Peanut butter cups. After giving his little sister 5 lollipops, how many pieces of candy did Brent have left?"""
    kit_kat = 5
    hershey_kisses = 3 * kit_kat
    nerds = 8
    lollipops = 11
    baby_ruth = 10
    reese_pb_cups = baby_ruth / 2
    total_candy = kit_kat + hershey_kisses + nerds + lollipops + baby_ruth + reese_pb_cups
    total_candy -= 5  # Brent gives little sister 5 lollipops
    result = total_candy
    return result

print(solution())