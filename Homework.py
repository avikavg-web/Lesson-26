import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
everything = chars + number
password = "".join(random.choice(everything) for _ in range (12))
list = list(password)
random.shuffle(list)
print("".join(list))