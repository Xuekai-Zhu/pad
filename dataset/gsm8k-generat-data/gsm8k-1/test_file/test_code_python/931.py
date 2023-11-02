def solution():
    """Fern is trying to decide between buying the Widgeteer 3000, which makes 60 widgets an hour, and the WidgetMaster 9000, which makes 45 widgets an hour. Each widget sells for $6. How much more money will Fern make from the Widgeteer 3000 vs. the WidgetMaster 9000 if it runs 24 hours a day for a month with 30 days?"""
    widgeteer_production = 60 * 24
    widgetmaster_production = 45 * 24
    widget_price = 6
    days_in_month = 30
    hours_in_day = 24
    widgeteer_profit = widgeteer_production * widget_price * days_in_month * hours_in_day
    widgetmaster_profit = widgetmaster_production * widget_price * days_in_month * hours_in_day
    difference = widgeteer_profit - widgetmaster_profit
    result = difference
    return result

print(solution())