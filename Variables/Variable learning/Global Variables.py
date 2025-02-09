# Global Variables mövzusunu yenidən sadə və rahat izah edim ki, tam başa düşəsən.
#
# Global dəyişən nədir?
# Global dəyişənlər funksiyaların xaricində elan olunur və proqramın hər yerində istifadə oluna bilir.
#
# Məsələn:
#
# python
# Copy
# Edit
# x = 10  # Global dəyişən
#
# def goster():
#     print("Dəyişən x:", x)
#
# goster()  # Nəticə: Dəyişən x: 10
# Niyə buna "global" deyirik?
# Çünki bu dəyişən proqramın bütün sahəsində (global sahədə) görünür və istifadə edilə bilir.
#
# Global dəyişəni funksiyanın içində dəyişmək
# Global dəyişəni funksiyanın içində dəyişmək istəyirsənsə, global açar sözündən istifadə etməlisən.
#
# Məsələn:
#
# python
# Copy
# Edit
# x = 10  # Global dəyişən
#
# def deyis():
#     global x  # Global dəyişənə müraciət
#     x = x + 5  # Dəyişən artırılır
#
# deyis()
# print(x)  # Nəticə: 15
# Əgər global açar sözünü istifadə etməsən, yeni lokal dəyişən yaradılır və bu, global dəyişəni dəyişdirmir.
#
# Global və lokal dəyişənlər
# Global dəyişənlər: Funksiyaların xaricində elan olunanlar.
# Lokal dəyişənlər: Funksiyaların daxilində yaradılanlar və yalnız həmin funksiyada istifadə olunur.
# Nümunə:
#
# python
# Copy
# Edit
# x = 10  # Global dəyişən
#
# def lokal_nümunə():
#     x = 20  # Lokal dəyişən
#     print("Lokal x:", x)
#
# lokal_nümunə()  # Nəticə: Lokal x: 20
# print("Global x:", x)  # Nəticə: Global x: 10
# Sən bu mövzunu necə daha yaxşı başa düşərsən?
# Sadə sözlər: Nəyi harada dəyişmək istədiyini dəqiqləşdirmək üçün nümunələrə bax.
# Təcrübə: Özün kiçik kod parçaları yaz və necə işlədiyini yoxla.
# Sual ver: Hansı hissədə çətinlik çəkirsənsə, mənə deyə bilərsən. 😊
# İndi başa düşmədiyin yeri izah edim, ya da başqa bir nümunə göstərim?

