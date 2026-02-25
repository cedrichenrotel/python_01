#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 10:08:43 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/25 17:13:14 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Module demonstrating inheritance through a garden plant hierarchy."""


class Plant:
    """Base class for all garden plants."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize core plant attributes."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Plant subclass representing decorative flowers."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize flower with color attribute."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Print a blooming message."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Plant subclass representing trees with shade-producing capabilities."""

    def __init__(self, name: str, height: int, age: int,
                 diameter: int) -> None:
        """Initialize tree with trunk diameter."""
        super().__init__(name, height, age)
        self.diameter = diameter

    def shadow_area_calculation(self) -> int:
        """Calculate and return the estimated shade area."""
        return int(1.56 * self.diameter) if self.height > 0 else 0

    def produce_shade(self) -> None:
        """Print the calculated shade area."""
        area = self.shadow_area_calculation()
        print(f"{self.name} provides {area} square meters of shade")


class Vegetable(Plant):
    """Plant subclass representing edible vegetables."""

    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """Initialize vegetable with harvest and nutrition data."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def harvest_info(self) -> None:
        """Display nutritional information."""
        print(f"{self.name} is rich in {self.nutritional_value}")


def specification_plant(obj: Plant) -> None:
    """Identify the plant type and display its specific characteristics."""
    if isinstance(obj, Flower):
        print(f"{obj.name}(Flower): {obj.height}cm, {obj.age} days, "
              f"{obj.color} color")
        obj.bloom()
    elif isinstance(obj, Tree):
        print(f"{obj.name}(Tree): {obj.height}cm, {obj.age} days, "
              f"{obj.diameter}cm diameter")
        obj.produce_shade()
    else:
        print(f"{obj.name} (vegetable): {obj.height}cm, "
              f"{obj.age} days, {obj.harvest_season} harvest")
        obj.harvest_info()


def main():
    """Main entry point to simulate a diverse garden."""
    garden = [
        Flower("Rose", 25, 30, "red"),
        Tree("Oak", 500, 1825, 50),
        Vegetable("Tomato", 80, 90, "April", "vitamine C"),
    ]

    print("=== Garden Plant Types ===\n")
    for plant in garden:
        specification_plant(plant)
        print()


if __name__ == "__main__":
    main()
