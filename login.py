import re
import time

from selenium.webdriver.common.by import By

class Login:

    def __init__(self, driver):
        self.driver = driver
        self.email = (By.ID, "email")
        self.password = (By.XPATH, "//input[@id='password']")
        self.btn_enviar = (By.XPATH, "//button[@type='submit']")
        self.btn_imagen = (By.XPATH, "//img[@src='/assets/rengoku.webp']")
        self.btn_cerrar_sesion = (By.XPATH, "//a[contains(.,'Logout')]")

    def login(self, email, password):
        """Automatiza el proceso de registro"""
        if not self.validar_email(email):
            print("Email inválido")
            return False
        if not self.validar_password(password):
            print("Contraseña inválida")
            return False
        self.formulario_login(email, password)
        self.boton_login()
        return True

    def formulario_login(self, email, password):
        """Rellena los campos de usuario y contraseña"""
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)

    def boton_login(self):
        """Hace clic en el botón de login"""
        self.driver.find_element(*self.btn_enviar).click()

    def cerrar_sesion(self):
        self.driver.find_element(*self.btn_imagen).click()
        time.sleep(3)
        self.driver.find_element(*self.btn_cerrar_sesion).click()

    def cerrar_ventana(self):
        span_close = self.driver.find_element(By.XPATH, "//span[contains(text(),'Close')]")
        self.driver.execute_script("arguments[0].click();", span_close)

    def validar_email(self, email):
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

    def validar_password(self, password):
        return (
                len(password) == 8 and
                any(c.isupper() for c in password) and
                any(c.islower() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in "!@#$%^&*()_+-=[]{};:'\"\\|,.<>/?~" for c in password)
        )