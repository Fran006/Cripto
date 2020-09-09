import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def spawn_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    #crar cuenta
    driver.get("https://www.dbsbeautystore.cl/tienda/index.php?route=account/register")
    print("Empezo")
    time.sleep(5)
    nombre = driver.find_element_by_name("firstname")
    nombre.send_keys("Francisca")
    print("nombre")
    apellido = driver.find_element_by_name("lastname")
    apellido.send_keys("Carrasco")
    email = driver.find_element_by_name("email")
    email.send_keys("francisca.cb@gmail.com")
    telefono = driver.find_element_by_name("telephone")
    telefono.send_keys("+56964476490")
    rut = driver.find_element_by_name("company")
    rut.send_keys("194318529")
    direccion = driver.find_element_by_name("address_1")
    direccion.send_keys("Soto Aguilar")
    numero = driver.find_element_by_name("city")
    numero.send_keys("1780")
    zona = driver.find_element_by_name("zone_id")
    zona.send_keys("pedro")
    contra = driver.find_element_by_name("password")
    contra.send_keys("Jaleita01")
    contra2 = driver.find_element_by_name("confirm")
    contra2.send_keys("Jaleita01")
    politicas = driver.find_element_by_name("agree")
    politicas.click()
    boton = driver.find_element_by_xpath('//input[@type="submit"][@value="Continuar"]')
    boton.click()

    #iniciar sesión    
    driver.get("https://www.dbsbeautystore.cl/tienda/index.php?route=account/login")
    email = driver.find_element_by_name("email")
    email.send_keys("francisca.cb@gmail.com")
    contra = driver.find_element_by_name("password")
    contra.send_keys("Jaleita01")
    boton = driver.find_element_by_xpath('//input[@type="submit"][@value="Iniciar sesión"]')
    boton.click()

    #restablecer contraseña
    driver.get("https://ilovemaquillaje.es/index.php?route=account/forgotten")
    time.sleep(5)
    email = driver.find_element_by_name("email")
    email.send_keys("francisca.cb@gmail.com")
    boton = driver.find_element_by_xpath('//input[@type="submit"][@value="Continuar"]')
    boton.click()

    #cambiar contraseña
    driver.get("https://www.dbsbeautystore.cl/tienda/index.php?route=account/login")
    email = driver.find_element_by_name("email")
    email.send_keys("bruno.a.gomez.j@gmail.com")
    contra = driver.find_element_by_name("password")
    contra.send_keys("jaleita01")
    boton = driver.find_element_by_xpath('//input[@type="submit"][@value="Iniciar sesión"]')
    boton.click()
    driver.get("https://www.dbsbeautystore.cl/tienda/index.php?route=account/password")
    print("listo para cambiar")
    time.sleep(5)
    contra1 = driver.find_element_by_name("password")
    contra1.send_keys("jaleita01")
    contra2 = driver.find_element_by_name("confirm")
    contra2.send_keys("jaleita01")
    boton2 = driver.find_element_by_xpath('//input[@type="submit"][@value="Continuar"]')
    boton2.click()

    #fuerza bruta
    driver.get("https://www.dbsbeautystore.cl/tienda/index.php?route=account/login")
    contador=0
    for i in range(1, 100):
        email = driver.find_element_by_name("email")
        email.send_keys("francisca.cb@gmail.com")
        contra = driver.find_element_by_name("password")
        contra.send_keys("Jaleita01")
        boton = driver.find_element_by_xpath('//input[@type="submit"][@value="Iniciar sesión"]')
        boton.click()
        contador=contador+1
        print(contador)
    

    

    return driver

spawn_browser()
