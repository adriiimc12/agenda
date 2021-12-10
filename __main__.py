from contacto import Contacto
from menu import Menu



def crear_agenda():
    c1 = Contacto("Adrián", "612.123.563", "c1@gmail.es")
    c2 = Contacto("Luis", "782.841,673", "c2@gmail.es")
    c3 = Contacto("Juan", "632.124.166", "c2@gmail.es")
    agenda = Menu()
    agenda.agregar_contacto(c1)
    agenda.agregar_contacto(c2)
    agenda.agregar_contacto(c3)
    return agenda

prueba = crear_agenda()
prueba.abrir_menu()
