class Menu:
    
    def __init__(self):
        self.__contactos = []
        self.ejecutado = False

    def agregar_contacto(self, contacto):
        self.__contactos.append(contacto)
        
    def listar_contacto(self):
        for c in self.__contactos:
            print(str(c))

    def buscar_contacto(self, nombre):
        for c in self.__contactos:
            if(c.get_nombre() == nombre):
                return c                  

    def editar_contacto(self, nombre):
        for c in self.__contactos:
            if(c.get_nombre == nombre):
                nombre = input("Escribe un nuevo nombre: ")
                c.set_nombre(nombre)

    def cerrar_menu(self):
        self.ejecutado = False
        return self.ejecutado
        
    def abrir_menu(self):
        self.ejecutado = True
        while(self.ejecutado == True):
            self.muestra_menu()
            self.leer_opcion()
    
    def muestra_menu(self):
        print("--¿QUÉ PRETENDES HACER?--")
        print("| 1. Nombrar Contacto:  |")
        print("| 2. Buscar Contacto:   |")
        print("| 3. Editar Contacto:   |")
        print("| 4. Cerrar Agenda:     |")
        print("-------------------------")
        
    def leer_opcion(self):

        opcion = int(input())

        if(opcion == 1):
            self.listar_contacto()
        elif(opcion == 2):
            nombre = input("Dime el nombre del contacto:")
            self.buscar_contacto(nombre)
        elif(opcion == 3):
            nombre = input("Dime el nombre del contacto:")
            self.editar_contacto(nombre)
        elif(opcion == 4):
            self.cerrar_menu()
        


        '''
    def editar_contacto(self, nombre):
        for c in self.__contactos:
            if(c["nombre"] == nombre):
                c["nombre"] = input("Escribe un nuevo nombre: ")   
'''