import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def spawn_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)

    #crear cuenta
    driver.get("https://ilovemaquillaje.es/index.php?route=account/register")
    time.sleep(5)
    nombre = driver.find_element_by_name("firstname")
    nombre.send_keys("Bruno")
    apellido = driver.find_element_by_name("lastname")
    apellido.send_keys("Gomez")
    email = driver.find_element_by_name("email")
    email.send_keys("bruno.a.gomez.j@gmail.com")
    telefono = driver.find_element_by_name("telephone")
    telefono.send_keys("+56985497633")
    contra = driver.find_element_by_name("password")
    contra.send_keys("Jaleita01")
    contra2 = driver.find_element_by_name("confirm")
    contra2.send_keys("Jaleita01")
    print("Empezo")
    boton = driver.find_element_by_name("agree")
    boton.click()
    print("boton listo")
    boton2 =  driver.find_element_by_xpath('//input[@type="submit"][@value="Continuar"]')
    boton2.click()


    #iniciar sesion
    driver.get("https://ilovemaquillaje.es/index.php?route=account/login")
    email = driver.find_element_by_name("email")
    email.send_keys("bruno.a.gomez.j@gmail.com")
    contra = driver.find_element_by_name("password")
    contra.send_keys("Jaleita01")
    boton = driver.find_element_by_xpath('//input[@type="submit"][@value="Acceder"]')
    boton.click()

    #restablecer contraseña
    driver.get("https://www.dbsbeautystore.cl/tienda/index.php?route=account/forgotten")
    time.sleep(5)
    email = driver.find_element_by_name("email")
    email.send_keys("francisca.cb@gmail.com")
    boton = driver.find_element_by_xpath('//input[@type="submit"][@value="Continuar"]')
    boton.click()

    #cambiar contraseña
    driver.get("https://ilovemaquillaje.es/index.php?route=account/login")
    email = driver.find_element_by_name("email")
    email.send_keys("bruno.a.gomez.j@gmail.com")
    contra = driver.find_element_by_name("password")
    contra.send_keys("Jaleita01")
    boton = driver.find_element_by_xpath('//input[@type="submit"][@value="Acceder"]')
    boton.click()
    driver.get("https://ilovemaquillaje.es/index.php?route=account/password")
    print("listo para cambiar")
    time.sleep(5)
    contra1 = driver.find_element_by_name("password")
    contra1.send_keys("jaleita01")
    contra2 = driver.find_element_by_name("confirm")
    contra2.send_keys("jaleita01")
    boton2 = driver.find_element_by_xpath('//input[@type="submit"][@value="Continuar"]')
    boton2.click()


    
    #fuerza bruta
    driver.get("https://ilovemaquillaje.es/index.php?route=account/login")
    print("Comienzo")
    contador=0

    for i in range(1, 100):
        email = driver.find_element_by_name("email")
        email.send_keys("francisca.cb@gmail.com")
        contra = driver.find_element_by_name("password")
        contra.send_keys("contraseñaincorrecta")
        boton = driver.find_element_by_xpath('//input[@type="submit"][@value="Acceder"]')
        boton.click()
        contador=contador+1
        print(contador)
    
    return driver

spawn_browser()
