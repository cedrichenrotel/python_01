#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 08:15:14 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/24 19:09:41 by cehenrot        ###   ########.fr        #
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

    @classmethod
    def create_garden_network(cls, list_garderner: list) -> "GardenManager":
        instance = cls()
        for garderner in list_garderner:
            if garderner in list_garderner:
                instance.list_garden[garderner] = []
        return instance

    def add_list(self, garderner: str, plant: object) -> None:
        if garderner not in self.list_garden:
            self.list_garden[garderner] = []
        self.list_garden[garderner].append(plant)

    class GardenStats:
        @staticmethod
        def growth_total(plant_list: list) -> int:
            total_height = 0
            for plant in plant_list:
                total_height += plant.get_height()
            return total_height

        @staticmethod
        def Plants_added(manager: object) -> int:
            total_plant = 0
            for plant in manager:
                total_plant += 1
            return total_plant

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
        def nb_garderner(garderner_dict: dict) -> int:
            return len(garderner_dict)

        @staticmethod
        def secure_height(plant_list: list) -> str:
            for plant in plant_list:
                if plant.get_height() <= 0:
                    return ("Error, incorrect plant height [REJECT]")
            return ("True [OK]")

        @staticmethod
        def print_list_garderen(plant_list: list) -> None:
            for plant in plant_list:
                base = f"- {plant.name}: {plant.get_height()}cm"
                if isinstance(plant, PrizeFlower):
                    base += f" {plant.color} flower (blooming), Prize points: "
                    base += f"{plant.score}"
                elif isinstance(plant, FloweringPlant):
                    base += f" {plant.color} flower (blooming)"
                print(base)


def main():
    manager = GardenManager()
    manager.add_list("Cedric", FloweringPlant("Rose", 10, "black"))
    manager.add_list("Cedric", FloweringPlant("Iris", -15, "white"))
    manager.add_list("Cedric", PrizeFlower("flower", 5, "yello", 5))
    manager.add_list("Cedric", PrizeFlower("Rose", 15, "white", 3))
    manager.add_list("Cannelle", PrizeFlower("Rose", 5, "red", 3))
    manager.add_list("Cannelle", FloweringPlant("Iris", 10, "yello"))

    cedric_plants = manager.list_garden["Cedric"]
    cannelle_plants = manager.list_garden["Cannelle"]

    height_total = GardenManager.GardenStats.growth_total(cedric_plants)
    total_plant = GardenManager.GardenStats.Plants_added(cedric_plants)
    nb_garderner = GardenManager.GardenStats.nb_garderner(manager.list_garden)
    score_cedric = GardenManager.GardenStats.garden_score(cedric_plants)
    score_cannelle = GardenManager.GardenStats.garden_score(cannelle_plants)
    check_height = GardenManager.GardenStats.secure_height(cedric_plants)

    print("=== Garden Management System Demo ===")
    print()
    print("=== Cedric's Garden Report ===")
    print("Plants in garden:")
    GardenManager.GardenStats.print_list_garderen(cedric_plants)
    print()
    print(f"Plants added: {total_plant}, "
          f"Total growth: {height_total}cm")
    GardenManager.GardenStats.print_is_instance(cedric_plants)
    print()
    print(f"Height validation test: {check_height}")
    print(f"Garden scores - Cedric: {score_cedric}, "
          f"Cannelle: {score_cannelle}")
    print(f"Total gardens managed: {nb_garderner}")


if __name__ == "__main__":
    main()
