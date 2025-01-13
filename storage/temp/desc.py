import json
import os

from JsonUtils import JsonUtils
from ObjectItem import ObjectItem


class Menu:

    def printKeys(self, obj, path=""):
        if obj is None:
            print(f"\n\t{path}:\tNull")
            return
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_path = f"{path}.{key}" if path else key
                self.printKeys(value, new_path)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                new_path = f"{path}[{index}]"
                self.printKeys(item, new_path)
        else:
            print(f"\t{path}:\t{obj}")

    def clearTerminal(self):
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Linux/Unix/Mac/Termux
            os.system('clear')

    def waitAnyKey(self):
        return input("\nPara sair digite qualquer tecla exceto as opções citadas no menu\n\nEscolha uma opção: ")

    def waitAnyKeyBack(self):
        return input("\nDigite [ e ] para sair ou qualque tecla \"Any key\" para continuar: ")

    def __init__(self):
        self.json_utils = JsonUtils()
        self.data = []

        while True:
            self.showMenu()
            user_input = self.waitAnyKey().lower()

            if user_input == '1':
                self.addObject()
                user_input = self.waitAnyKeyBack().lower()
                if user_input == 'e':
                    break

            elif user_input == '2':
                self.readObjects()
                user_input = self.waitAnyKeyBack().lower()
                if user_input == 'e':
                    break

            elif user_input == '3':
                self.updateValue()
                user_input = self.waitAnyKeyBack().lower()
                if user_input == 'e':
                    break

            elif user_input == '4':
                self.delObjects()
                user_input = self.waitAnyKeyBack().lower()
                if user_input == 'e':
                    break

            elif user_input == '0':
                self.clearTerminal()
                continue
            else:
                break

    def showMenu(self):
        self.clearTerminal()
        print("\n" + "="*44)
        print("\tPrograma de Criação de Base\n")
        print("\tEscolha uma das opções abaixo:\n")
        print("\t1. Adicionar Objeto")
        print("\t2. Ler Objetos")
        print("\t3. Alterar Objeto")
        print("\t4. Deletar Objetos")
        print("\t0. Voltar ao Menu Principal\n")
        print("="*44 + "\n")

    def delObjects(self):
        self.clearTerminal()
        print("\n" + "-"*44)
        self.json_utils.del_obj()
        self.json_utils.sv_file()
        self.updateData()
        print("\n" + "-"*44)

    def updateValue(self):
        self.clearTerminal()
        print("\n" + "-"*44)
        print("\nAlteração de dados, digite as informações necessárias\n")

        for obj in self.data:
            print("\nItem:")
            self.printKeys(obj)

        path = input("\nDigite o caminho da variavel do arquivo: ")
        cv = input("Digite o valor atual: ")
        nv = input("Digite o novo valor: ")

        keys = path.split('.')
        for obj in self.data:
            temp = obj

            for key in keys[:-1]:
                temp = temp.get(key, {})
            if str(temp.get(keys[-1])) == str(cv):
                temp[keys[-1]] = nv
                print(f"\nAtualização completa. Novo estado dos dados:\n")

                for obj in self.data:
                    print("\nItem:")
                    self.printKeys(obj)


                #self.json_utils.set_obj(self.data)
                #self.json_utils.sv_file()
                #self.updateData()

        self.json_utils.set_obj(self.data)
        print("\n" + "-"*44)


    def addObject(self):
        self.clearTerminal()
        print("\n" + "-"*44)
        print("\nAdicionar Novo Objeto\n")
        self.objectItem = ObjectItem()
        self.newObj = self.objectItem.newObject()
        print("\nNovo Objeto Criado:\n\n")
        self.printKeys(self.newObj)
        self.json_utils.update_jsn(self.newObj)
        self.updateData()
        print("\n" + "-"*44)

    def updateData(self):
        try:
            with open("../../report.json", "r") as file:
                self.data = json.load(file)

        except FileNotFoundError:
            print("\tErro: O arquivo 'report.json' não foi encontrado.")
        except json.JSONDecodeError:
            print("\tErro: O arquivo 'report.json' não é um JSON válido.")


    def readObjects(self):
        self.clearTerminal()
        print("\n" + "-"*44)
        print("\nLer Objetos do Arquivo 'report.json'\n\n")

        self.updateData()

        for obj in self.data:
            print("\nItem:")
            self.printKeys(obj)

        print("\n" + "-"*44)



if __name__ == "__main__":

    m = Menu()

