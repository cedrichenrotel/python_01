# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 08:13:35 by cehenrot        #+#    #+#               #
#  Updated: 2026/02/16 11:16:15 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name, size, age):
        self.name = name
        self.size = size
        self.age = age

    def print(self):
        print(f"{self.name}, {self.size}, {self.age}")


if __name__ == "__main__":
    p2 = Plant("Iris", "15cm", "6 days old")
    p3 = Plant("Rose", "30 cm", "5 days old")
    p1 = Plant("Chene", "600 cm", "123 days old")
    my_plant = [p1, p2, p3]

    print("=== Garden Plant Registry ===")
    for i in range(3):
        my_plant[i].print()
