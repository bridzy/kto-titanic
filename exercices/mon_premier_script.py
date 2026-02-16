import unittest

message = "C'est mon premier script !!!"
print(message)

je_change_de_type = 1
print(type(je_change_de_type))
je_change_de_type = "coucou"
print(type(je_change_de_type))


"""
Count names with more than seven letters
"""
def names(prenoms: list[str]) -> int:
    more_than_seven = 0

    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
            print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
        else:
            print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")

    return more_than_seven


def saluer(nom: str) -> str:
    return "Bonjour " + nom


class TestNamesMethod(unittest.TestCase):
    def test_names(self) -> None:
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = names(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)


if __name__ == "__main__":
    prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
    print("Nombre de prénoms dont le nombre de lettres est supérieur à 7 : " + str(names(prenoms=prenoms)))

    print(saluer("Alice"))  # Affiche : Bonjour Alice

    unittest.main()