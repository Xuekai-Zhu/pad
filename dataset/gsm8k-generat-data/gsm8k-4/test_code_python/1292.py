def solution():
    """A town is holding a fireworks display for New Year’s Eve. They light enough fireworks to show the full year then light enough fireworks to write “HAPPY NEW YEAR” in the sky.
    They then light another 50 boxes of fireworks as part of the display. Each box of fireworks contains 8 fireworks.
    If it takes 6 fireworks to display a number and 5 fireworks to display a letter, how many fireworks are lit during the display?"""
    # Define the number of fireworks needed to display each digit
    digit_fireworks = 6
    
    # Define the number of fireworks needed to display each letter
    letter_fireworks = 5
    
    # Define the message to be displayed in the sky
    message = "HAPPY NEW YEAR"
    
    # Calculate the total number of fireworks needed to display the year
    year_fireworks = sum([digit_fireworks for digit in str(2022)])
    
    # Calculate the total number of fireworks needed to display the message
    message_fireworks = sum([letter_fireworks if char.isalpha() else digit_fireworks for char in message])
    
    # Calculate the total number of fireworks lit during the display
    total_fireworks = year_fireworks + message_fireworks + (50 * 8)
    
    return total_fireworks

print(solution())