#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 13:19:25 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/20 10:51:33 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    nb_plant: int = 0

    def __init__(self, name: str, size: int, days: int) -> None:
        self.name = name
        self.size = size
        self.days = days
        Plant.nb_plant += 1

    def printf(self) -> None:
        print(f"Created: {self.name} "
              f"({self.size} cm, {self.days} day old)")


if __name__ == "__main__":
    lst_p = [Plant("Rose", 25, 30), Plant("Oak", 200, 365),
             Plant("Cactus", 5, 90), Plant("Sunflower", 80, 45),
             Plant("Fern", 15, 120)]

    print("=== Plant Factory Output ===")
    for i in range(Plant.nb_plant):
        lst_p[i].printf()
    print(f"Total plants created: {i + 1}")
