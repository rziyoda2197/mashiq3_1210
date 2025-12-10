#7 - misol
my_list = ["dog", "cat", "mouse"]
bosh_harf = [x[0] for x in my_list]
print(bosh_harf)

#8 - misol
son = [-5, 3, -1, 0, 7, -2]
musbatlar = [x for x in son if x > 0]
print(musbatlar)

#9 - misol
natija = ["juft" if x % 2 == 0 else "toq" for x in range(1, 11)]
print(natija)
