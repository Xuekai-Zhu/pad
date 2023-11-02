def solution():
    """Prince Thaddeus slew 100 dragons with his mighty sword, while Prince Arthur, using a spear, slew three quarters as many dragons as Prince Thaddeus. Using a rusty iron axe, Prince Walter slew twice as many dragons as Prince Arthur. But Prince Bruce, having forgot his sword at home, slew one-fifth as many dragons as Prince Walter using a nail file. How many Dragons has Prince Bruce slain?"""
    thaddeus_dragons = 100
    arthur_dragons = thaddeus_dragons * 0.75
    walter_dragons = arthur_dragons * 2
    bruce_dragons = walter_dragons * 0.2
    result = bruce_dragons
    return result

print(solution())