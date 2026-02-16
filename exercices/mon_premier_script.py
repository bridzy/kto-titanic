import unittest

message = "C'est mon premier script !!!"
print(message)

je_change_de_type = 1
print(type(je_change_de_type))
je_change_de_type = "coucou"
print(type(je_change_de_type))


def names(prenoms: list[str]) -> int:
    """Compter les prénoms qui ont plus de 7 lettres (et afficher le message associé)."""
    more_than_seven = 0

    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
            print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
        else:
            print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")

    return more_than_seven


prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
more_than_seven = names(prenoms)
print("Nombre de prénoms dont le nombre de lettres est supérieur à 7 : " + str(more_than_seven))
print("----------------------------------------------------------------------")


def saluer(nom: str) -> str:
    return "Bonjour " + nom
#print(saluer("Alice"))  # Affiche : Bonjour Alice


class TestNamesMethod(unittest.TestCase):
    def test_names(self) -> None:
        prenoms_test = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        self.assertEqual(names(prenoms_test), 4)


if __name__ == "__main__":
    unittest.main() 