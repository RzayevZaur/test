# Dəyişənlərin yaradılması
# Python-da dəyişən elan etmək əmri yoxdur.
#
# Dəyişən ilk dəfə ona dəyər təyin etdiyiniz anda yaradılır.


# x = 5
# y = "John"
# print(x)
# print(y)

# Dəyişənlərin hər hansı bir xüsusi tiplə elan edilməsinə ehtiyac yoxdur
# və hətta təyin edildikdən sonra növü dəyişə bilər.

# x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)


# Əgər dəyişənin məlumat tipini təyin etmək istəyirsinizsə, bu, tökmə ilə edilə bilər.

# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# print(x)
# print(y)
# print(z)


# Funksiya ilə dəyişənin məlumat tipini əldə edə bilərsiniz type().

# x = 5
# y = "John"
# print(type(x))
# print(type(y))








# Tək və ya Cüt Sitatlar?
# Sətir dəyişənləri tək və ya cüt dırnaq işarələrindən istifadə etməklə elan edilə bilər:


x = "John"
# is the same as
# x = 'John'

print(x)



# Python-da dəyişənlər adlara həssasdır (case-sensitive). Yəni, böyük və kiçik hərflər fərqli dəyişənlər kimi qəbul edilir.
# a və A iki tamamilə fərqli dəyişəndir:
# a = 4 – kiçik hərflə yazılan a dəyişəni ədədi dəyəri 4-ə bərabərdir.
# A = "Sally" – böyük hərflə yazılan A dəyişəni isə mətn (string) dəyəri "Sally"-ə bərabərdir.


x = 10
X = 20
print(x)  # Nəticə: 10
print(X)  # Nəticə: 20
