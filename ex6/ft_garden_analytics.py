#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 08:15:14 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/25 10:11:39 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    plant_created: list = []

    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.set_height(height)

    def set_height(self, value: int) -> bool:
        if value > 0:
            self.__height = value
            return True
        else:
            self.__height = 0
        return False

    def get_height(self) -> int:
        return self.__height


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int,
                 color: str, score: int) -> None:
        super().__init__(name, height, color)
        self.score = score


class GardenManager:
    def __init__(self) -> None:
        self.list_garden = {}
        self.list_garderner = []

    def add_list(self, garderner: str, plant: object) -> None:
        if garderner not in self.list_garden:
            self.list_garden[garderner] = []
        self.list_garden[garderner].append(plant)

    class GardenStats:

        @staticmethod
        def print_is_instance(plant_list: list) -> None:
            stats = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}
            for plant in plant_list:
                if (isinstance(plant, PrizeFlower)):
                    stats["PrizeFlower"] += 1
                elif (isinstance(plant, FloweringPlant)):
                    stats["FloweringPlant"] += 1
                elif (isinstance(plant, Plant)):
                    stats["Plant"] += 1
            print(f"Plant types: {stats['Plant']} regular, "
                  f"{stats['FloweringPlant']} flowering, "
                  f"{stats['PrizeFlower']} prize flowers")

        @staticmethod
        def garden_score(plant_list: list) -> int:
            total_score = 0
            for plant in plant_list:
                total_score += plant.get_height()
                if isinstance(plant, PrizeFlower):
                    total_score += plant.score
            return (total_score)

        @staticmethod
        def print_nb_garderner(garderner_dict: dict) -> None:
            print(f"Total gardens managed: {len(garderner_dict)}")

        @staticmethod
        def secure_height(plant_list: list) -> str:
            for plant in plant_list:
                if plant.get_height() <= 0:
                    return ("Error, incorrect plant height [REJECT]")
            return ("True [OK]")

        @staticmethod
        def print_list_garderen(plant_list: list) -> None:
            print("Plants in garden:")
            for plant in plant_list:
                base = f"- {plant.name}: {plant.get_height()}cm"
                if isinstance(plant, PrizeFlower):
                    base += f" {plant.color} flower (blooming), Prize points: "
                    base += f"{plant.score}"
                elif isinstance(plant, FloweringPlant):
                    base += f" {plant.color} flower (blooming)"
                print(base)

        @staticmethod
        def print_added_plant(garderner: str, plant_list: list) -> None:
            for plant in plant_list:
                print(f"Added {plant.name} to {garderner}'s garden")

        @staticmethod
        def print_plant_grow(garderner: str, plant_list: list) -> None:
            print(f"{garderner} is helping all plants grow...")
            for plant in plant_list:
                new_height = plant.get_height() + 1
                plant.set_height(new_height)
                print(f"{plant.name} grew 1cm")

        @staticmethod
        def growth_total(plant_list: list) -> int:
            total_height = 0
            for plant in plant_list:
                total_height += plant.get_height()
            return total_height

        @staticmethod
        def Plants_added(plant_list: list) -> int:
            total_plant = 0
            for plant in plant_list:
                total_plant += 1
            return total_plant


def main():
    manager = GardenManager()
    manager.add_list("Cedric", Plant("Oak Tree", 101))
    manager.add_list("Cedric", FloweringPlant("Rose", 26, "red"))
    manager.add_list("Cedric", PrizeFlower("Sunflower", 51, "yellow", 10))
    manager.add_list("Cannelle", FloweringPlant("Sunflower", 40, "white"))
    manager.add_list("Cannelle", PrizeFlower("Rose", 22, "red", 10))
    manager.add_list("Cannelle", FloweringPlant("Iris", 20, "yello"))

    cedric_plants = manager.list_garden["Cedric"]
    cannelle_plants = manager.list_garden["Cannelle"]

    height_total = GardenManager.GardenStats.growth_total(cedric_plants)
    total_plant = GardenManager.GardenStats.Plants_added(cedric_plants)
    score_cedric = GardenManager.GardenStats.garden_score(cedric_plants)
    score_cannelle = GardenManager.GardenStats.garden_score(cannelle_plants)
    check_height = GardenManager.GardenStats.secure_height(cedric_plants)

    print("=== Garden Management System Demo ===")
    print()
    GardenManager.GardenStats.print_added_plant("Cedric", cedric_plants)
    print()
    GardenManager.GardenStats.print_plant_grow("Cedric", cedric_plants)
    print()
    print("=== Cedric's Garden Report ===")
    GardenManager.GardenStats.print_list_garderen(cedric_plants)
    print()
    print(f"Plants added: {total_plant}, "
          f"Total growth: {height_total}cm")
    GardenManager.GardenStats.print_is_instance(cedric_plants)
    print()
    print(f"Height validation test: {check_height}")
    print(f"Garden scores - Cedric: {score_cedric}, "
          f"Cannelle: {score_cannelle}")
    GardenManager.GardenStats.print_nb_garderner(manager.list_garden)


if __name__ == "__main__":
    main()
