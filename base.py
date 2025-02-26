from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Base:
    def __init__(self, driver_path, base_url):
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.base_url = base_url
        self.driver.maximize_window()

    def abrir_pagina(self):
        """Abre la URL base directamente"""
        self.driver.get(self.base_url)

    def cerrar(self):
        """Cierra el navegador"""
        self.driver.quit()