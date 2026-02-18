# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 13:54:52 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/18 14:07:41 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self._height = height
        self._age = age

    def set_height(self, value: int):
        match (value < 0):
            case True:
                print(f"operation attempted: height {value}cm"
                      " [REJECTED]")
            case False:
                print(f"Height updated: height {value}cm [OK]")
                self._height = value

    def set_age(self, value: int):
        match (value < 0):
            case True:
                print(f"operation attempted: age {value} days"
                      " [REJECTED]")
            case False:
                print(f"Age updated: age {value} days [OK]")
                self._age = value

    def get_name(self):
        return self.name

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


def main():
    plant = SecurePlant("Rose", 0, 0)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.name}")
    plant.set_height(25)
    plant.set_age(-30)
    print(f"Current plant: {plant.get_name()}"
          f"({plant.get_height()}cm {plant.get_age()} days)")


if __name__ == "__main__":
    main()
