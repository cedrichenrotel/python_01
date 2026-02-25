#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 13:54:52 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/25 17:11:10 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Module providing a secure interface for plant data management."""


class SecurePlant:
    """A plant class using private attributes and validated setters."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant with a public name and private height/age."""
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, value: int) -> None:
        """Update height only if the provided value is non-negative."""
        match (value < 0):
            case True:
                print(f"operation attempted: height {value}cm [REJECTED]")
            case False:
                print(f"Height updated: height {value}cm [OK]")
                self.__height = value

    def set_age(self, value: int) -> None:
        """Update age only if the provided value is non-negative."""
        match (value < 0):
            case True:
                print(f"\noperation attempted: age {value} days [REJECTED]\n"
                      "Security: Negative age rejected")
            case False:
                print(f"Age updated: age {value} days [OK]")
                self.__age = value

    def get_name(self) -> str:
        """Return the public name of the plant."""
        return self.name

    def get_height(self) -> int:
        """Return the private height value."""
        return self.__height

    def get_age(self) -> int:
        """Return the private age value."""
        return self.__age


def main():
    """Execute the garden security system simulation."""
    plant = SecurePlant("Rose", 0, 0)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.name}")
    plant.set_height(25)
    plant.set_age(-30)
    print()
    print(f"Current plant: {plant.get_name()} "
          f"({plant.get_height()}cm, {plant.get_age()} days)")


if __name__ == "__main__":
    main()
