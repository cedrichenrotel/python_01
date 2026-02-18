# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 10:08:43 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/18 15:57:21 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: int, age: int) -> (None):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> (None):
        super().__init__(name, height, age)
        self.colore = color

    def bloom(self) -> (None):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 diameter: int) -> (None):
        super().__init__(name, height, age)
        self.diameter = diameter

    def shadow_area_calculation(self) -> (int):
        if (self.height > 0):
            return self.height * (self.diameter / 10)
        else:
            return 0

    def produce_shade(self) -> (None):
        area = self.shadow_area_calculation()
        print(f"The {self.name} provides {area} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> (None):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def harvest_info(self) -> (None):
        print(f"{self.name} is rich in {self.nutritional_value}")


def specification_plant(obj: Plant) -> (None):
    if (type(obj).__name__ == "Flower"):
        print(f"{obj.name}(Flower): {obj.height}cm, {obj.age} days, "
              f"{obj.colore} color")
        obj.bloom()
    elif (type(obj).__name__ == "Tree"):
        print(f"{obj.name}(Tree): {obj.height}cm, {obj.age} days, "
              f"{obj.diameter}cm diameter")
        obj.produce_shade()
    else:
        print(f"{obj.name} (vegetale): {obj.height}cm, "
              f"{obj.age} days, {obj.harvest_season} harvest")
        obj.harvest_info()


def main():
    garden = [
        Flower("Rose", 30, 25, "red"),
        Flower("iris", 5, 7, "white"),
        Tree("apple tree", 70, 2410, 25),
        Tree("Oak", 8, 50000, 25),
        Vegetable("Tomato", 5, 18, "April", "vitamine C"),
        Vegetable("carrot", 5, 18, "March", "vitamine A")
    ]

    print("=== Garden Plant Types ===")
    print()
    for i in garden:
        specification_plant(i)
        print()


if __name__ == "__main__":
    main()
