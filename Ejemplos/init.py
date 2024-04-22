# Forma 1 de llamar las credenciales
#*************************************************
from credenciales import usuario

n_, p_ = usuario()
print(n_,p_)



# Forma 2 de llamar las credenciales
#*************************************************
import json

# Ruta al archivo JSON
ruta_json = "variables.json"

# Cargar el contenido del archivo JSON
with open(ruta_json, "r") as archivo:
    datos = json.load(archivo)

# Acceder a las variables desde el JSON
var1 = datos["nombre"]
var2 = datos["pass"]
var3 = datos["key"]
var4 = datos["endp"]

# Utilizar las variables en tu código
print(f"Var1: {var1}, Var2: {var2}, Var3: {var3}, Var4: {var4}")
