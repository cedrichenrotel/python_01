#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 08:15:14 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/25 17:36:18 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Module for managing multiple gardens with nested statistical analysis
tools."""


class Plant:
    """Base class for all plants with height validation."""
    plant_created: list = []

    def __init__(self, name: str, height: int) -> None:
        """Initialize plant and set its validated height."""
        self.name = name
        self.set_height(height)

    def set_height(self, value: int) -> bool:
        """Set height if positive; otherwise, default to 0."""
        if value > 0:
            self.__height = value
            return True
        self.__height = 0
        return False

    def get_height(self) -> int:
        """Return the current height of the plant."""
        return self.__height


class FloweringPlant(Plant):
    """Subclass for plants that possess a flower color."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize flowering plant with a specific color."""
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    """Subclass for competitive flowers with a performance score."""

    def __init__(self, name: str, height: int, color: str, score: int) -> None:
        """Initialize prize flower with a bonus score."""
        super().__init__(name, height, color)
        self.score = score


class GardenManager:
    """Manages associations between gardeners and their collections of
    plants."""

    def __init__(self) -> None:
        """Initialize empty garden and gardener tracking."""
        self.list_garden = {}
        self.list_garderner = []

    def add_list(self, garderner: str, plant: object) -> None:
        """Assign a plant to a specific gardener's collection."""
        if garderner not in self.list_garden:
            self.list_garden[garderner] = []
        self.list_garden[garderner].append(plant)

    class GardenStats:
        """Nested class providing static utility methods for garden
        analysis."""

        @staticmethod
        def print_is_instance(plant_list: list) -> None:
            """Count and print the frequency of each plant type."""
            stats = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}
            for plant in plant_list:
                if isinstance(plant, PrizeFlower):
                    stats["PrizeFlower"] += 1
                elif isinstance(plant, FloweringPlant):
                    stats["FloweringPlant"] += 1
                elif isinstance(plant, Plant):
                    stats["Plant"] += 1
            print(f"Plant types: {stats['Plant']} regular, "
                  f"{stats['FloweringPlant']} flowering, "
                  f"{stats['PrizeFlower']} prize flowers")

        @staticmethod
        def garden_score(plant_list: list) -> int:
            """Calculate total score based on height and prize points."""
            total_score = 0
            for plant in plant_list:
                total_score += plant.get_height()
                if isinstance(plant, PrizeFlower):
                    total_score += plant.score
            return total_score

        @staticmethod
        def print_nb_garderner(garderner_dict: dict) -> None:
            """Print the total number of gardens currently managed."""
            print(f"Total gardens managed: {len(garderner_dict)}")

        @staticmethod
        def secure_height(plant_list: list) -> str:
            """Validate that all plants in the list have a positive height."""
            for plant in plant_list:
                if plant.get_height() <= 0:
                    return "Error, incorrect plant height [REJECT]"
            return "True [OK]"

        @staticmethod
        def print_list_garderen(plant_list: list) -> None:
            """Print detailed summary of all plants in a specific garden."""
            print("Plants in garden:")
            for plant in plant_list:
                base = f"- {plant.name}: {plant.get_height()}cm"
                if isinstance(plant, PrizeFlower):
                    base += f" {plant.color} flower (blooming), "
                    base += f"Prize points: {plant.score}"
                elif isinstance(plant, FloweringPlant):
                    base += f" {plant.color} flower (blooming)"
                print(base)

        @staticmethod
        def print_added_plant(garderner: str, plant_list: list) -> None:
            """Confirm the addition of plants to a gardener's list."""
            for plant in plant_list:
                print(f"Added {plant.name} to {garderner}'s garden")

        @staticmethod
        def print_plant_grow(garderner: str, plant_list: list) -> None:
            """Simulate 1cm of growth for every plant in a gardener's list."""
            print(f"{garderner} is helping all plants grow...")
            for plant in plant_list:
                if plant.get_height() > 0:
                    plant.set_height(plant.get_height() + 1)
                    print(f"{plant.name} grew 1cm")

        @staticmethod
        def growth_total(plant_list: list) -> int:
            """Return the sum of all plant heights in the list."""
            return sum(plant.get_height() for plant in plant_list)

        @staticmethod
        def Plants_added(plant_list: list) -> int:
            """Return the total count of plants in the list."""
            return len(plant_list)


def main():
    """Main entry point to demonstrate the Garden Management System."""
    manager = GardenManager()
    manager.add_list("Cedric", Plant("Oak Tree", 101))
    manager.add_list("Cedric", FloweringPlant("Rose", -26, "red"))
    manager.add_list("Cedric", PrizeFlower("Sunflower", 51, "yellow", 10))
    manager.add_list("Cannelle", FloweringPlant("Sunflower", 40, "white"))
    manager.add_list("Cannelle", PrizeFlower("Rose", 22, "red", 10))
    manager.add_list("Cannelle", FloweringPlant("Iris", 20, "yello"))

    ced_p = manager.list_garden["Cedric"]
    can_p = manager.list_garden["Cannelle"]

    print("=== Garden Management System Demo ===\n")
    GardenManager.GardenStats.print_added_plant("Cedric", ced_p)
    print()
    GardenManager.GardenStats.print_plant_grow("Cedric", ced_p)
    print("\n=== Cedric's Garden Report ===")
    GardenManager.GardenStats.print_list_garderen(ced_p)

    print(f"\nPlants added: {GardenManager.GardenStats.Plants_added(ced_p)}, "
          f"Total growth: {GardenManager.GardenStats.growth_total(ced_p)}cm")
    GardenManager.GardenStats.print_is_instance(ced_p)

    print("\nHeight validation test: "
          f"{GardenManager.GardenStats.secure_height(ced_p)}")
    print("Garden scores - Cedric: "
          f"{GardenManager.GardenStats.garden_score(ced_p)}, "
          f"Cannelle: {GardenManager.GardenStats.garden_score(can_p)}")
    GardenManager.GardenStats.print_nb_garderner(manager.list_garden)


if __name__ == "__main__":
    main()
