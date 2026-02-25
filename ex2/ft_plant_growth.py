#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 11:16:50 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/25 10:46:39 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, size: int, age: int) -> None:
        self.name = name
        self.size = size
        self.age = age

    def day(self) -> None:
        self.size += 1
        self.age += 1

    def print_plant(self) -> None:
        print(f"{self.name}:", f"{self.size} cm, {self.age} days old")


if __name__ == "__main__":
    p = Plant("rose", 25, 30)
    size_start = p.size
    print("=== day 1 ===")
    p.print_plant()
    print("=== day 7 ===")
    for i in range(6):
        p.day()
    p.print_plant()
    growth = (p.size - size_start)
    print(f"Growth this week: +{growth}cm")
