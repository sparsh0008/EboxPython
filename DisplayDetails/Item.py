class Item:
    def __init__(self, iid, item_name, company_name, price):
        self.iid = iid
        self.item_name = item_name
        self.company_name = company_name
        self.price = price

    def display(self):
        print("Item ID: ", self.iid)
        print("Item Name: ", self.item_name)
        print("Company Name: ", self.company_name)
        print("Price of Item: ", self.price, "Rs")
