from datetime import datetime, timedelta

сегодня = datetime.now()
вчера = сегодня - timedelta(days=1)
завтра = сегодня + timedelta(days=1)

print("Yesterday:", вчера.strftime('%d.%m'))
print("Today", сегодня.strftime('%d.%m'))
print("Tommorow:", завтра.strftime('%d.%m'))
