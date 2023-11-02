def solution():
    """Brian goes fishing twice as often as Chris, but catches 2/5 times fewer fish than Chris per trip. If Brian caught 400 fish every time he went fishing, how many fish did they catch altogether if Chris went fishing 10 times?"""
    # Define Brian's catch
    brian_catch = 400

    # Calculate Chris's catch
    chris_catch = brian_catch / (1 - 2/5)
    
    # Calculate the total catch
    total_catch = (brian_catch * 2) + (chris_catch * 10)

    # Display the total catch
    result = total_catch
    return result

print(solution())