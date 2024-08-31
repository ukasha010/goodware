import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Setup Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome (no UI)
service = Service(r'C:\Users\ukasha\Desktop\goodware\chromedriver.exe')  # Path to your ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

def download_software(software_url):
    # Navigate to the software page
    driver.get(software_url)
    time.sleep(2)  # Allow time for the page to load

    # Find and click the "Download Now" button
    try:
        
        download_button = driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/article/div[2]/div/a')
        download_button.click()
        time.sleep(2)  # Allow time for redirection

        # Confirm download button and click
        driver.get(driver.current_url)  # Get redirected URL
        time.sleep(2)
        download_button = driver.find_element(By.XPATH, '/html/body/main/div/div/div/article/section[1]/div[1]/div/a')
        download_button.click()

        print("Download started.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Example software URL
    software_list = [
        'https://download.cnet.com/planet-vpn-free-vpn-proxy/3000-2092_4-78704597.html',
        # Add more URLs here
    ]
    
    for software_url in software_list:
        download_software(software_url)

if __name__ == "__main__":
    main()
    driver.quit()
