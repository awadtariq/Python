import datetime

Do_you_like_pineapple_on_pizza = True
Are_you_wearing_socks = True
Is_today_the_weekend = False

print("do you like pineapple on your pizza", Do_you_like_pineapple_on_pizza)
print("Are you wearing socks", Are_you_wearing_socks)
print("is today the weekend", Is_today_the_weekend)

current_day = datetime.datetime.now().weekday()

is_weekend = current_day >= 5

print("Is it the weekend", is_weekend)