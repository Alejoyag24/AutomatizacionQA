import time

from selenium.webdriver.common.by import By

from base import Base
from registro import Registro
from login import Login

if __name__ == "__main__":
    # Configuración webdriver
    driver_path = "C:/Drivers/chromedriver.exe"
    base_url = "https://test-qa.inlaze.com/auth/"
    web_driver = Base(driver_path, base_url)

    # Abrir página
    web_driver.abrir_pagina()
    time.sleep(5)
    # llamado clase registro
    app_inlaze = Registro(web_driver.driver)
    app_inlaze.botonEnlace()
    time.sleep(5)
    # llenar formulario registro
    usuario_valido = app_inlaze.registro("Mara Dona", "Mara2019@gmail.com", "Dona777*", "Dona777*")
    time.sleep(10)

    if usuario_valido:
        app_login = Login(web_driver.driver)
        app_login.cerrar_ventana()
        login_succes = app_login.login("Mara2019@gmail.com", "Dona777*")
        time.sleep(10)
        # cerrar sesion
        if login_succes:
            app_login.cerrar_sesion()

        time.sleep(5)

    # Cerrar el navegador
    web_driver.cerrar()
