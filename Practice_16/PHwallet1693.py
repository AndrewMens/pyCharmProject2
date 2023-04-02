class Customers:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"{self.first_name} {self.second_name}. {self.city}. Баланс: {self.balance} руб."

    def get_gest(self):
        return f"{self.first_name} {self.second_name}, {self.city}"

customer_1 = Customers("Иван", "Петров", "Москва", "50")
customer_2 = Customers("Ivanka", "Trump", "Los Angeles", "1000")

print(customer_1)

gest_list = [customer_1, customer_2]

for gest in gest_list:
    print(gest.get_gest())



