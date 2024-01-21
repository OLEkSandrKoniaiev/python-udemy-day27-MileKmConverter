# def add(*args):
#     result = 0
#     for n in args:
#         result += n
#     print(result)


# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     # print(kwargs["add"])
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)

# # Work with class

class Car:
    def __init__(self, **kw):
        # # Обов'язкові параметри
        # self.make = kw["make"]
        # self.model = kw["model"]

        # # Функція get у випадку коли аргумент не зазначено повертає значення None
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan",
             # model="GT-R"
             )
print(my_car.make)
print(my_car.model)

# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
#
#
# all_aboard(4, 7, 3, 0, x=10, y=64)
