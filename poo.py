from abc import ABC, abstractmethod

# Définition d'une classe abstraite
class Animal(ABC):
    
    # Méthode abstraite
    @abstractmethod
    def crier(self):
        pass
    
# Classe dérivée qui implémente la méthode abstraite
class Chien(Animal):
    def crier(self):
        print("Wouaf!")

# Instanciation de la classe dérivée
chien = Chien()

# Appel de la méthode
chien.crier()