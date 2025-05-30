from temperature import Temperature


class Calorie:
    """Represents optimal calorie amount a person needs per day"""

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10*self.weight + 6.5*self.height + 5 - self.temperature*10
        return result

if __name__ == "__main__":
    temperature = Temperature("finland", "turku").get()
    calorie = Calorie(weight=60, height=170, age=35, temperature=temperature)
    print(calorie.calculate())