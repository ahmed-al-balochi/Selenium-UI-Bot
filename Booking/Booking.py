from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class Booking(webdriver.Chrome):
    BASE_URL = "https://www.booking.com/"

    def __init__(self, driver_path='/usr/bin/chromedriver'):
        service = Service(driver_path)
        super(Booking, self).__init__(service=service)
    
    def land_first_page(self):
        self.get(self.BASE_URL)
        self.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']").click()
        self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]').click()
        self.find_element(By.XPATH, "//button[.//span[contains(text(),'U.S. Dollar')]]").click()
        print("Offer pop-up closed!")

    def enter_dest(self, city):
        try:
            dest = self.find_element(By.ID, ':rh:')
            dest.send_keys(city)
            print(city, " entered")
        except:
            self.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']").click()
            print("Offer pop-up closed!")


    def enter_dates(self, check_in, check_out):
        self.find_element(By.CSS_SELECTOR,'button[data-testid="date-display-field-start"]').click()
        self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in}"]').click()

        self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out}"]').click()
        print('Dates entered: ', check_in, check_out)

    def enter_memebers(self, adults):
        self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]').click()
        adults_no = int(self.find_element(By.XPATH, '(//span[@class="d723d73d5f"])[1]').text)
        if adults_no > adults:
            for i in range(-adults_no, -adults):
                self.find_element(By.XPATH, '(//div[@class="bfb38641b0"]/button)[1]').click()
                print(i, "clicked on remove button")
        elif adults_no < adults:
            for i in range(adults_no, adults):
                self.find_element(By.XPATH, '(//div[@class="bfb38641b0"]/button)[2]').click()
                print(i, "clicked on add button")

    def submit(self):
        self.find_element(By.XPATH, '//button[span[text()="Search"]]').click()
        print('button [search] clicked')

    def sort_data(self):
        #time.sleep(3) # sorters button only fully loads after 3 secs and the bot clicks it way too early to get the popup  
        try:
            WebDriverWait(self, 10).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]'))
            )
            self.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]').click()
            print('button[data-testid="sorters-dropdown-trigger"] clicked')
        except:
            print('button[data-testid="sorters-dropdown-trigger"] failed click')

        try:
            sort_button = WebDriverWait(self, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-id="review_score_and_price"]'))
            )
            sort_button.click()
            print('button[data-id="review_score_and_price"] clicked')
        except:
            print('button[data-id="review_score_and_price"] failed click')
    
    def select_room(self):
        current_tab = self.current_window_handle
        WebDriverWait(self, 10).until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@data-testid="property-card"]/div)[1]'))
        ).click()

        WebDriverWait(self, 10).until(EC.number_of_windows_to_be(2))
        for window_handle in self.window_handles:
            if window_handle != current_tab:
                self.switch_to.window(window_handle)
                break
        print("switched to room!")
    
    def reserve_room(self):
        room = WebDriverWait(self, 5).until(
            EC.element_to_be_clickable((self.find_element(By.CSS_SELECTOR, 'select[data-testid="select-room-trigger"]')))
        )
        select_room = Select(room)
        select_room.select_by_value("1")

        WebDriverWait(self, 5).until(
            EC.visibility_of((self.find_element(By.CLASS_NAME, 'hprt-reservation-cta')))
        ).click()
        print('reserve button[class="hprt-reservation-cta"] clicked')
        