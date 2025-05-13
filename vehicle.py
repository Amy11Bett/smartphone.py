# Smartphone Class

class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def make_call(self, phone_number):
        print(f"Calling {phone_number} using {self.brand} {self.model}...")

    def check_battery(self):
        print(f"{self.brand} {self.model} battery is at {self.battery_life}%.")

    def charge(self):
        self.battery_life = 100
        print(f"{self.brand} {self.model} is fully charged!")

# SmartphoneWithCamera Class (Inheritance & Polymorphism)

class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_quality):
        super().__init__(brand, model, battery_life)
        self.camera_quality = camera_quality

    def make_call(self, phone_number):
        print(f"Making a video call to {phone_number} using {self.brand} {self.model}...")

    def take_picture(self):
        print(f"Taking a picture with {self.camera_quality} camera on {self.brand} {self.model}.")

# Creating an instance of SmartphoneWithCamera
camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S21", 80, "108MP")

camera_phone.make_call("987-654-3210")
camera_phone.take_picture()
camera_phone.check_battery()

