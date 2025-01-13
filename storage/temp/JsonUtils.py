import json
import os


class JsonUtils:

    def __init__(self, nam="report.json"):
        self.jsn_arr = []
        self.nam = nam

    def add_obj(self, obj):
        if isinstance(obj, dict):
            if obj not in self.jsn_arr:
                self.jsn_arr.append(obj)

    def del_obj(self):
        self.jsn_arr = []

    def set_obj(self, new_obj):
        self.jsn_arr = new_obj
        self.sv_file()

    def sv_file(self):
        path = os.path.join(os.getcwd(), self.nam)

        with open(path, "w", encoding="utf-8") as arquivo:
            json.dump(self.jsn_arr, arquivo, ensure_ascii=False, indent=4)

        print(f"\nArquivo salvo em: {path}")

    def update_jsn(self, obj):

        path = os.path.join(os.getcwd(), self.nam)

        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as file:
                    ctx = file.read()

                    if not ctx.strip():
                        self.jsn_arr = []
                    else:

                        dat = json.loads(ctx)

                        if isinstance(dat, list):
                            self.jsn_arr = dat

                        else:
                            raise ValueError("O arquivo JSON não contém um JSONArray válido.")
            except json.JSONDecodeError:
                raise ValueError("O arquivo não é um JSON válido.")
        else:
            self.jsn_arr = []

        self.add_obj(obj)
        self.sv_file()