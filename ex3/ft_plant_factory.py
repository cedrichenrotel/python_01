#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 13:19:25 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/25 17:09:47 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Module for a plant factory tracking the total count of created instances."""


class Plant:
    """Represents a plant and tracks the total number of Plant instances."""
    nb_plant: int = 0

    def __init__(self, name: str, size: int, days: int) -> None:
        """Initialize plant and increment the global plant counter."""
        self.name = name
        self.size = size
        self.days = days
        Plant.nb_plant += 1

    def printf(self) -> None:
        """Display the plant's current specifications."""
        print(f"Created: {self.name} "
              f"({self.size} cm, {self.days} days old)")


if __name__ == "__main__":
    """Main execution to batch create plants and report the total count."""
    lst_p = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")
    for i in range(Plant.nb_plant):
        lst_p[i].printf()

    print(f"Total plants created: {Plant.nb_plant}")
