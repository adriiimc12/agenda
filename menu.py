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
            if(c["nombre"] == nombre):
                c["nombre"] = input("Escribe un nuevo nombre: ")   

    def cerrar_menu(self):
        self.ejecutado = False
        return self.ejecutado
        
    def abrir_menu(self):
        self.ejecutado = True
        while(self.ejecutado == True):
            self.muestra_menu()
            self.leer_opcion()
    
    def muestra_menu(self):
        print("--¿QUE PRETENDES HACER?--")
        print("| 1. Nombrar Contacto: ")
        print("| 2. Buscar Contacto: ")
        print("| 3. Modificar Contacto: ")
        print("| 4. Cerrar Agenda: ")
        print("-----------------------")
        
    def leer_opcion(self):
        opcion = int(input())
    
        try:
            opcion = -1
            while((opcion > 4) or (opcion < 1)):
                opcion = int(input(">"))
        except:
            print("Error")

        if (opcion == 1):
            self.listar_contacto()
        elif(opcion == 2):
            self.buscar_contacto()
        elif(opcion == 3):
            self.editar_contacto()
        elif(opcion == 4):
            self.cerrar_menu()
        