class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.__interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.__interest_rate
        print(f"Interest calculated: {interest}")
        return interest


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0, minimum_balance=500):
        super().__init__(account_number, balance)
        self.__minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.get_balance() - amount >= self.__minimum_balance:
            super().withdraw(amount)
        else:
            print("Withdrawal denied. Minimum balance requirement not met.")


# Example usage:
savings = SavingsAccount("SA1236", 1000)
savings.deposit(500)
savings.calculate_interest()
savings.withdraw(200)

current = CurrentAccount("CA456", 1000)
current.withdraw(600)
current.withdraw(400)





########Problem 2: Employee Management
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class RegularEmployee(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Manager(Employee):
    def __init__(self, name, salary, team_bonus):
        super().__init__(name, salary)
        self.team_bonus = team_bonus

    def calculate_salary(self):
        return self.salary + self.team_bonus
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class RegularEmployee(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Manager(Employee):
    def __init__(self, name, salary, team_bonus):
        super().__init__(name, salary)
        self.team_bonus = team_bonus

    def calculate_salary(self):
        return self.salary + self.team_bonus


if __name__ == "__main__":
    regular_employee = RegularEmployee("Alice", 50000, 5000)
    contract_employee = ContractEmployee("Bob", 50, 160)
    manager = Manager("Charlie", 80000, 10000)

    print(f"{regular_employee.name}'s salary: ${regular_employee.calculate_salary()}")
    print(f"{contract_employee.name}'s salary: ${contract_employee.calculate_salary()}")
    print(f"{manager.name}'s salary: ${manager.calculate_salary()}")




#######Problem 3: Vehicle Rental
class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days


class Car(Vehicle):
    def __init__(self, model, rental_rate, seating_capacity):
        super().__init__(model, rental_rate)
        self.seating_capacity = seating_capacity

    def calculate_rental(self, days):
        base_cost = self.rental_rate * days
        additional_charge = 10 * self.seating_capacity * days
        return base_cost + additional_charge


class Bike(Vehicle):
    def __init__(self, model, rental_rate, bike_type):
        super().__init__(model, rental_rate)
        self.bike_type = bike_type

    def calculate_rental(self, days):
        base_cost = self.rental_rate * days
        if self.bike_type == "Electric":
            surcharge = 20 * days
        else:
            surcharge = 0
        return base_cost + surcharge


class Truck(Vehicle):
    def __init__(self, model, rental_rate, cargo_capacity):
        super().__init__(model, rental_rate)
        self.cargo_capacity = cargo_capacity

    def calculate_rental(self, days):
        base_cost = self.rental_rate * days
        capacity_charge = 50 * self.cargo_capacity * days
        return base_cost + capacity_charge


if __name__ == "__main__":
    # Create instances of each vehicle type
    car = Car("Toyota Camry", 50, 5)  # $50/day, 5 seats
    bike = Bike("Mountain Bike", 20, "Mountain")  # $20/day, Mountain type
    electric_bike = Bike("Electric Bike", 20, "Electric")  # $20/day, Electric type
    truck = Truck("Ford F-150", 100, 2)  # $100/day, 2 tons cargo capacity


    days = 3
    print(f"Rental cost for {car.model} for {days} days: ${car.calculate_rental(days)}")
    print(f"Rental cost for {bike.model} for {days} days: ${bike.calculate_rental(days)}")
    print(f"Rental cost for {electric_bike.model} for {days} days: ${electric_bike.calculate_rental(days)}")
    print(f"Rental cost for {truck.model} for {days} days: ${truck.calculate_rental(days)}")

