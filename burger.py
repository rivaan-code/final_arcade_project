class Subway_Sanwich:

    bun_types = {1:"Italian",2:"9-Grain wheat",3:"Flatbread", 4:"Italian Herbs and Cheese", 5:"Monterey Cheddar", 5:"Parmesan Cheddar", 6:"Wraps"}
    patty_types = {1:"Veggie",2:"Grilled Chicken",3:"Roast Beef", 4:"Steak and Cheese", 5:"Tuna", 5:"Turkey", 6:"Chicken Teriyaki", 7:"No Patty"}
    bread_toppings = {1:"lettuce", 2:"tomatoes", 3:"onions",4:"cucembers",5:"pickles",6:"jalapenos",7:"bacon",8:"avacodo",9:"no toppings"}
    sauces = {1:"mayonnaise", 2:"mustard", 3:"honey mustard", 4:"ranch", 5:"buffalo sauce", 6:"No Sauce"}

    def __init__(self, bun_type, patty_type, cheese=None, toppings=None, sauce=None, price=0.0):
        self.bun_type = bun_type
        self.patty_type = patty_type
        self.cheese = cheese
        self.toppings = toppings if toppings is not None else []
        self.sauce = sauce
        self.price =price

    def add_topping(self, topping):
        """Adds a topping to the burger."""
        self.toppings.append(topping)
        # print(f"Added {topping} to the burger.")

    def add_cheese(self, cheese):
        self.cheese = cheese

    def calculate_total_price(self):
        if self.bun_type != "":
            self.price += 3
        if self.patty_type != "":
            self.price += 3
        if self.cheese == 'y':
            self.price += 2
        if len(self.toppings) > 0:
            self.price += len(self.toppings) * .50

        return self.price

    def describe(self):
        description = f"\n\nYour delicious {self.patty_types[int(self.patty_type)]} burger on a {(self.bun_types[int(self.bun_type)])} bread."
        if self.cheese == 'y':
            description += f" With cheese."
        if self.toppings:
            description += f" Topped with: {', '.join(self.toppings)}."
        if self.sauce:
            description += f"Dressed with {','.join(self.sauces[int(self.sauce)])} is ready!"

        return description

    def display(self,menu):
        for key, value in menu.items():
            print(f"{key}. {value}")

    def order_burger(self):
        print("BREAD CHOICES:")
        self.display(self.bun_types)
        self.bun_type = input("\nEnter your bun type : ")

        print("\nPATTY CHOICES:")
        self.display(self.patty_types)
        self.patty_type = input("\nEnter your patty type : ")

        user_cheese = input("\nDo you want cheese (y/n) : ")
        if user_cheese.lower() == 'y':
            self.cheese = user_cheese.lower()

        print("\nTOPPING CHOICES:")
        self.display(self.bread_toppings)
        user_toppings = input("\nEnter your choice of multiple Toppings (comma separated) : ")
        for item in user_toppings.split(","):
            self.toppings.append(self.bread_toppings[int(item)])

        print("\nSAUCE CHOICES:")
        self.display(self.sauces)
        user_sauce = input("\nEnter your choice of sauce : ")


b = Subway_Sanwich({}, {}, '', [],  [], 0.0)
b.order_burger()
print(b.describe())
print(f"\nYour total is : ${b.calculate_total_price()}")
print("\nThank you for ordering. Enjoy your organic delicious Sanwich!!\n")

