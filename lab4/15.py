from datetime import datetime

current_date = datetime.now()
no_microsecond = current_date.replace(microsecond=0)

print("Date with microsecond:", current_date)
print("Date without microsecond:", no_microsecond)
