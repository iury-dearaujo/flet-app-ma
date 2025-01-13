class ObjectItem:

    def __init__(self):
        self.objeto = None
        self.objetos = []
        self.initObj()

    def initObj(self):
        self.objeto = {"Nome": None, "Idade": None, "Origem": None}

    def newObject(self):
        for key in self.objeto.keys():
            value = input(f"Qual o valor para o {key}: ")
            self.objeto[key] = value
        self.objetos.append(self.objeto)
        return self.objeto
