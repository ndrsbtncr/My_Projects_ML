from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
import tkinter as tk

texto_guardado = ""  # Variable global para guardar el texto

def capturar_texto():
    global texto_guardado
    texto_ingresado = entrada.get()
    texto_guardado = texto_ingresado  # Guardar el texto en la variable global
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Captura de Texto")

etiqueta = tk.Label(ventana, text="Ingrese un texto:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton_capturar = tk.Button(ventana, text="Capturar Texto", command=capturar_texto)
boton_capturar.pack()

etiqueta_resultado = tk.Label(ventana, text="Texto guardado: ")
etiqueta_resultado.pack()

ventana.mainloop()



browser = webdriver.Chrome()

titulo = texto_guardado
link = f'https://www.indeed.com/career/{titulo.replace(" ","-")}/salaries'

browser.get(link)


sleep(5)  

periodo = 'MONTHLY'

select = Select(browser.find_element(By.ID, 'pay-period-selector'))
select.select_by_value(periodo)

sleep(5)  

elements = browser.find_elements(By.CLASS_NAME, 'css-15so73c.e19afand0')
salaries = browser.find_elements(By.CLASS_NAME, 'css-k60owf.e1wnkr790')

with open('indeed_info.txt', 'w') as archivo:

    for i in range(len(salaries)):
        company_name = elements[i].text
        salary_info = salaries[i].text.split()
        salary = salary_info[0]
        #print(f"{company_name}: {salary} per {periodo.lower()}")
        
        archivo.write(company_name + " " + salary + " " + periodo.lower() + '\n')

sleep(5)  
browser.quit()