
class Client:

# A simple class
# attribute
    name = "Danny"
    age = 45
    default = False
    profile = 'RSME'

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
        return None

    def info(self):
        print(f"The client name: {self.name} and age: {self.age}")

    def get_name(self):
        print('this is ', self.name)