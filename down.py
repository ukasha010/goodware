import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Selenium WebDriver
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment if needed

# Configure Chrome to automatically download files
prefs = {
    "download.default_directory": r"C:\Download\Benign",  # Update with your download directory
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

service = Service(r'C:\Users\ukasha\Desktop\goodware\chromedriver.exe')  # Path to your ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

def click_element(driver, element):
    try:
        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)  # Small delay to ensure the scroll effect
        # Click the element using JavaScript if it's being blocked
        driver.execute_script("arguments[0].click();", element)
    except Exception as e:
        print(f"Error while clicking the element: {e}")

def download_software(software_url):
    driver.get(software_url)
    try:
        wait = WebDriverWait(driver, 30)
        download_button_xpath = '/html/body/main/div/div/div[1]/article/div[2]/div/a'
        
        # Wait for the download button to be present and clickable
        download_button = wait.until(EC.presence_of_element_located((By.XPATH, download_button_xpath)))
        wait.until(EC.element_to_be_clickable((By.XPATH, download_button_xpath)))
        
        print("Download button found.")
        # driver.save_screenshot('screenshot_before_click.png')  # Take a screenshot before clicking
        click_element(driver, download_button)
        
        # Wait for redirection or new content
        time.sleep(10)  # Increased wait time for potential redirections or content loading

        print()

        cross_button_xpath = '/html/body/div[3]/div[2]/div[1]/button'
        cross_button = wait.until(EC.presence_of_element_located((By.XPATH, cross_button_xpath)))
        wait.until(EC.element_to_be_clickable((By.XPATH, cross_button_xpath)))
        
        print("Cross button found.")
        # driver.save_screenshot('cross_before_click.png')  # Take a screenshot before clicking
        click_element(driver, cross_button)

        try:
            # Update with XPath of the final download button or any indicator of successful download
            final_button_xpath = '/html/body/main/div/div/div/article/section[1]/div[1]/div/a'
            final_button = wait.until(EC.presence_of_element_located((By.XPATH, final_button_xpath)))
            
            print("Final download button found.")
            # driver.save_screenshot('screenshot_final_button.png')  # Take a screenshot before final click
            click_element(driver, final_button)

            print("Download started.")
        except Exception as e:
            print(f"Final button not found or another issue occurred: {e}")
            # driver.save_screenshot('screenshot_final_error.png')  # Take a screenshot for debugging

    except Exception as e:
        print(f"An error occurred: {e}")
        # driver.save_screenshot('screenshot_error.png')  # Take a screenshot in case of an error

def main():
    # Example software URL list
    software_list = [
        'https://download.cnet.com/planet-vpn-free-vpn-proxy/3000-2092_4-78704597.html',
        # Add more URLs here
    ]
    
    for software_url in software_list:
        download_software(software_url)

    input("Press Enter to close the browser...")

if __name__ == "__main__":
    main()
    # driver.quit()
