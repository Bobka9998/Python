# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
son = int(input('Istagan butun son kiriting: '))
for n in range(2,11):
  if not son%n:
    print(f'{son} soni {n} ga qoldiqsiz bo`linadi.')
  else:
    print(f'{son} soni {n} ga qoldiqsiz bo`linmaydi.')