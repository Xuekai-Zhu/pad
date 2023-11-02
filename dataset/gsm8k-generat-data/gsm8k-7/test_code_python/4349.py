def solution():
    mars_disappears = "12:10 AM"
    jupiter_delay = "2:41"
    uranus_delay = "3:16"

    # Convert Jupiter and Uranus delay times to minutes
    jupiter_delay_minutes = (2 * 60) + 41
    uranus_delay_minutes = (3 * 60) + 16

    # Calculate the time Uranus first appears in the sky (in minutes)
    mars_disappears_minutes = (12 * 60) + 10
    uranus_appears_minutes = mars_disappears_minutes + jupiter_delay_minutes + uranus_delay_minutes

    # Convert the final result back to time (in the format HH:MM AM/PM)
    hours = uranus_appears_minutes // 60
    minutes = uranus_appears_minutes % 60
    meridian = "AM" if hours < 12 else "PM"
    hours = hours % 12
    if hours == 0:
        hours = 12
    result = "{:02d}:{:02d} {}".format(hours, minutes, meridian)
    return result

print(solution())