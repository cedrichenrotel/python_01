#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 11:02:32 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/23 07:40:06 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str, score: int) -> None:
        super().__init__(name, height, age, color)
        self.score = score


class GardenManager:

    def __init__(self, garden: str) -> None:
        self.garden = garden
        self.Plant = []

    class GardenStats:
        @staticmethod
        def growth_total(list_p) -> int:
            total_growth = 0
            for plant in list_p:
                total_growth += plant.height
            return total_growth

        def Plants_added(list_p) -> int:
            total_plant = 0
            for plant in list_p:
                total_plant += 1
            return total_plant

        def is_instance(list_p) -> None:
            stats = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}
            for plant in list_p:
                if (isinstance(plant, PrizeFlower)):
                    stats["PrizeFlower"] += 1
                elif (isinstance(plant, FloweringPlant)):
                    stats["FloweringPlant"] += 1
                elif (isinstance(plant, Plant)):
                    stats["Plant"] += 1
            print(f"Plant types: {stats["Plant"]} regular, {stats["FloweringPlant"]} flowering, "
                  f"{stats["PrizeFlower"]} prize flowers")


def main():
    # my_garden = [
    #     GardenManager("Cannelle"),
    #     GardenManager("Cédric"),
    #     GardenManager("Paul"),
    # ]
    my_garden = "Cannelle"
    list_p = [
        FloweringPlant("Rose", 10, 15, "black"),
        FloweringPlant("Iris", 12, 10, "pink"),
        PrizeFlower("Rose", 15, 10, "red", 2),
        PrizeFlower("Rose", 15, 10, "white", 3),
        Plant("Oak", 25, 30)
    ]
    height_total = GardenManager.GardenStats.growth_total(list_p)
    total_plant = GardenManager.GardenStats.Plants_added(list_p)
    print("=== Garden Management System Demo ===")
    print()
    print(f"=== {my_garden}'s Garden Report ===")

    print("Plants in garden:")
    print(f"Plants added: {total_plant}, "
          f"Total growth: {height_total}cm")
    GardenManager.GardenStats.is_instance(list_p)


if __name__ == "__main__":
    main()
