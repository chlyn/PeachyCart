class User:
    def __init__(self, first_name, last_name, email, phone_number, user_id, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.user_id = user_id
        self.password = password
        self.cart = {}
        self.wishlist = {}
        self.bank_account = {}

    def add_to_cart(self, product_id, product_name, quantity):
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'name': product_name, 'quantity': quantity}

        print(f"\"{product_name}\" has been successfully added to your cart.")

    def remove_from_cart(self, product_id):
        if product_id in self.cart:
            product_name = self.cart[product_id]['name']
            del self.cart[product_id]
            print(f"\"{product_name}\" has been successfully removed from your cart.")
        else:
            print(f"\"{product_name}\" could not be found in your cart. Please try again.")

    def display_cart(self):

        for product

    