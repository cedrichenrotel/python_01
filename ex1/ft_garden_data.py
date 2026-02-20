#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 08:13:35 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/20 09:38:13 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, size: int, age: int) -> None:
        self.name = name
        self.size = size
        self.age = age

    def print(self) -> None:
        print(f"{self.name}: {self.size}cm, {self.age} day old")


if __name__ == "__main__":
    p1 = Plant("Chene", 40, 200)
    p2 = Plant("Iris", 60, 123)
    p3 = Plant("Rose", 30, 15)
    my_plant = [p1, p2, p3]

    print("=== Garden Plant Registry ===")
    for i in range(3):
        my_plant[i].print()
