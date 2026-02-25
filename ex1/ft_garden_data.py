#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 08:13:35 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/25 17:05:49 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Module for managing and displaying a garden plant registry."""


class Plant:
    """Represents a plant with its characteristics."""

    def __init__(self, name: str, size: int, age: int) -> None:
        """Initialize plant with name, size (cm), and age (days)."""
        self.name = name
        self.size = size
        self.age = age

    def print(self) -> None:
        """Print plant details to the console."""
        print(f"{self.name}: {self.size}cm, {self.age} days old")


if __name__ == "__main__":
    # Create plant instances
    plants = [
        Plant("Chene", 40, 200),
        Plant("Iris", 60, 123),
        Plant("Rose", 30, 15)
    ]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.print()
