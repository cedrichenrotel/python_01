#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 11:16:50 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/25 17:08:15 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Module to simulate and track plant growth over time."""


class Plant:
    """Represents a plant that grows daily."""

    def __init__(self, name: str, size: int, age: int) -> None:
        """Initialize plant with its name, size (cm), and age (days)."""
        self.name = name
        self.size = size
        self.age = age

    def day(self) -> None:
        """Simulate one day of growth: increases size and age by 1."""
        self.size += 1
        self.age += 1

    def print_plant(self) -> None:
        """Display the current state of the plant."""
        print(f"{self.name}:", f"{self.size} cm, {self.age} days old")


if __name__ == "__main__":
    """Main execution to simulate a week of growth for a Rose."""
    p = Plant("rose", 25, 30)
    size_start = p.size

    print("=== day 1 ===")
    p.print_plant()

    print("=== day 7 ===")
    for _ in range(6):
        p.day()
    p.print_plant()

    growth = p.size - size_start
    print(f"Growth this week: +{growth}cm")
