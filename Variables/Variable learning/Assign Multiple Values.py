# Python dilində bir neçə dəyişənə bir sətirdə dəyər təyin etmək, kodu daha qısa və oxunaqlı
# saxlamağa kömək edir. Bu yanaşmaların fərqli halları və istifadələri aşağıda izah olunur:
#
#
# 1. Çox Dəyərdən Çox Dəyişənlərə Təyin
# Bir sətirdə birdən çox dəyişənə dəyər təyin etmək mümkündür. Bu üsul oxunaqlılığı artırır və dəyərləri dəyişənlərə eyni zamanda bölüşdürməyə imkan verir.
# Misal:

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)  # Orange
# print(y)  # Banana
# print(z)  # Cherry
# #

# Vacib Qeyd:
# Dəyişənlərin sayı dəyərlərin sayı ilə uyğun olmalıdır. Əks halda, Python ValueError qaytarır.
# Səhv nümunə:

# x, y = "Apple", "Orange", "Banana"  # ValueError: too many values to unpack
#
#
#
# 2. Bir Dəyəri Çox Dəyişənlərə Təyin
# Eyni dəyəri bir sətirdə birdən çox dəyişənə təyin etmək mümkündür. Bu üsul eyni məlumatı fərqli dəyişənlərdə saxlamaq üçün faydalıdır.
# Misal:

# x = y = z = "Orange"
# print(x)  # Orange
# print(y)  # Orange
# print(z)  # Orange


#
# 3. Kolleksiyanı Paketdən Çıxarmaq (Unpacking)
# Siyahı, tuple və digər kolleksiyalardan dəyərləri ayrı-ayrı
# dəyişənlərə çıxarmağa imkan verir. Bu yanaşma məlumatlarla
# işləmək üçün çox rahatdır.
# Misal:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  # apple
print(y)  # banana
print(z)  # cherry



