string = "Rabelo"
metod = "upper1"

# print(dir(string))
# print(string.lower())

# if hasattr(string,'lower'):
#     print("Has lower metod")
#     print(string.lower())
# else:
#     print("Does not have lower metod")

if hasattr(string,metod):
    print("Exist upper metod")
    print(getattr(string,metod)())
else:
    print("Does not have the metod",metod)