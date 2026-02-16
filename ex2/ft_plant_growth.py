# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 11:16:50 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/16 13:18:17 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name, size, age):
        self.name = name
        self.size = size
        self.age = age

    def day(self):
        self.size += 1
        self.age += 1

    def print(self):
        print(f"{self.name}:", f"{self.size} cm, {self.age} day old")


if __name__ == "__main__":
    p = Plant("rose", 25, 30)
    size_start = p.size
    print("=== day 1 ===")
    p.print()
    for day in range(6):
        p.day()
    print("=== day 7 ===")
    p.print()
    growth = (p.size - size_start)
    print(f"Growth this week: +{growth}cm")
