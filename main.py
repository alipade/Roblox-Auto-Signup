import random
import math
import string
import time
from colorama import init, Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

init()
ascii_art = """
▄▄▄        ▄▄▄▄· ▄▄▌             ▄▄▄· ▄• ▄▌▄▄▄▄▄          .▄▄ · ▪   ▄▄ •  ▐ ▄ ▄• ▄▌ ▄▄▄·
▀▄ █·▪     ▐█ ▀█▪██•  ▪         ▐█ ▀█ █▪██▌•██  ▪         ▐█ ▀. ██ ▐█ ▀ ▪•█▌▐██▪██▌▐█ ▄█
▐▀▀▄  ▄█▀▄ ▐█▀▀█▄██▪   ▄█▀▄     ▄█▀▀█ █▌▐█▌ ▐█.▪ ▄█▀▄     ▄▀▀▀█▄▐█·▄█ ▀█▄▐█▐▐▌█▌▐█▌ ██▀·
▐█•█▌▐█▌.▐▌██▄▪▐█▐█▌▐▌▐█▌.▐▌    ▐█ ▪▐▌▐█▄█▌ ▐█▌·▐█▌.▐▌    ▐█▄▪▐█▐█▌▐█▄▪▐███▐█▌▐█▄█▌▐█▪·•
.▀  ▀ ▀█▄▀▪·▀▀▀▀ .▀▀▀  ▀█▄▀▪     ▀  ▀  ▀▀▀  ▀▀▀  ▀█▄▀▪     ▀▀▀▀ ▀▀▀·▀▀▀▀ ▀▀ █▪ ▀▀▀ .▀   
"""

print(Fore.LIGHTRED_EX + ascii_art)
print('Made by https://github.com/sourcream-and-onion\n')

name_keyword = input('Name Keyword: ')
random_string_length = int(input('Random String Length: '))
password_length = int(input('Password Length: '))
random_gender_input = input('Random Gender (y/N): ')
if random_gender_input in ['y', 'Y']:
    pass
elif random_gender_input in ['n', 'N']:
    gender_you_want = input('Gender that you want (f/M): ')
    pass

months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']
years_list = ['1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999']
password_letters = ['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$&']
gender_choices = ['Male', 'Female']

def signup():
    random_username = name_keyword + ''.join(random.choices(string.ascii_uppercase, k=int(random_string_length)))
    password_string = password_letters[0]
    random_password = ''.join(random.choices(password_string, k=password_length))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--window-size=500,500")
    chrome_options.add_extension('nopeCHA.crx')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get('https://roblox.com/')

    def select_month():
        months_element = driver.find_element(By.XPATH, '/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div[1]/select')
        Select(months_element).select_by_value(random.choice(months_list))

    def select_day():
        days_element = driver.find_element(By.XPATH, '/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div[2]/select')
        Select(days_element).select_by_value(random.choice(days_list))

    def select_year():
        years_element = driver.find_element(By.XPATH, '/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div[3]/select')
        Select(years_element).select_by_value(random.choice(years_list))

    def fill_username():
        username_element = driver.find_element(By.XPATH, '/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/input')
        username_element.send_keys(random_username)

    def fill_password():
        password_element = driver.find_element(By.XPATH, '/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/input')
        
        password_element.send_keys(random_password)

    def select_gender():
        female_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[4]/div/div/button[1]')
        male_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[4]/div/div/button[2]')

        if random_gender_input in ['y', 'Y']:
            random_gender = random.choice(gender_choices)
            if random_gender == 'Female':
                female_button.click()
                pass
            elif random_gender == 'Male':
                male_button.click()
                pass
        elif random_gender_input in ['n', 'N']:
            if gender_you_want in ['f', 'F']:
                female_button.click()
            elif gender_you_want in ['m', 'M']:
                male_button.click()

    def click_signup_button():
        signup_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div[1]/div/div/div/button')
        while True:
            if signup_button.is_enabled():
                signup_button.click()
                break

    select_month()
    select_day()
    select_year()
    fill_username()
    fill_password()
    select_gender()
    click_signup_button()

    try:
        WebDriverWait(driver, math.inf).until(EC.url_to_be('https://www.roblox.com/home?nu=true'))

        with open('accounts.txt', 'a') as f:
            f.write(random_username + ':' + random_password + '\n')

        print('Signup Successfully')
        driver.close()
        return True
    except:
        print('Signup failed')
        return False

while signup():
    time.sleep(1)