import re

from selenium.webdriver.common.by import By

class Registro:

    def __init__(self, driver):
        self.driver = driver
        self.enlaceRegistro = (By.LINK_TEXT, "Sign up")
        self.username = (By.ID, "full-name")
        self.email = (By.ID, "email")
        self.password = (By.XPATH, "//input[@id='password']")
        self.btnvisual1 = (By.XPATH, "(//i[contains(@class,'fa-solid fa-eye')])[1]")
        self.confirm_password = (By.XPATH, "//input[contains(@id,'confirm-password')]")
        self.btnvisual2 = (By.XPATH, "(//button[contains(@type,'button')])[2]")
        self.btn_enviar = (By.XPATH, "//button[@type='submit']")

    def botonEnlace(self):
        """Hace clic en el botón de 'Registro' para ir a la página de registro"""
        self.driver.find_element(*self.enlaceRegistro).click()

    def registro(self, username, email, password, confirm_password):
        """Automatiza el proceso de registro"""

        if not self.validar_username(username):
            print("Username inválido (Debe tener al menos 2 palabras)")
            return False
        if not self.validar_email(email):
            print("Email inválido")
            return False
        if not self.validar_password(password):
            print("Contraseña inválida")
            return False
        if password != confirm_password:
            print("Las contraseñas no coinciden")
            return False

        self.formulario_registro(username, email, password, confirm_password)
        self.boton_registro()
        return True

    def formulario_registro(self, username, email, password, confirm_password):
        """Rellena los campos de registro"""
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.desactivar_boton(self.btnvisual1)
        self.driver.find_element(*self.confirm_password).send_keys(confirm_password)
        self.desactivar_boton(self.btnvisual2)

    def boton_registro(self):
        """Hace clic en el botón de registro"""
        self.driver.find_element(*self.btn_enviar).click()

    def desactivar_boton(self, boton):
        """Hace clic en el botón si no está activo"""
        elemento_btn = self.driver.find_element(*boton)
        if "active" in elemento_btn.get_attribute("class"):
            elemento_btn.click()

    def validar_username(self, username):
        return len(username.split()) >= 2

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