import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Selenium WebDriver with options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment for headless mode

# Configure Chrome to automatically download files
prefs = {
    "download.default_directory": r"C:\Download\Benign",  # Set your download directory
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize WebDriver
service = Service(r'C:\Users\ukasha\Desktop\goodware\chromedriver.exe')  # Update with your ChromeDriver path
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 30)

def click_element(element):
    """Scroll to and click an element."""
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)  # Allow time for the scroll effect
        driver.execute_script("arguments[0].click();", element)
    except Exception as e:
        print(f"Error clicking element: {e}")

def download_software():
    """Download software by navigating through download buttons and popups."""
    try:
        # Locate and click the main download button
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/article/div[2]/div/a')))
        print("Download button found.")
        click_element(download_button)
        time.sleep(10)  # Wait for potential redirects or loading

        # Close any popups that may appear
        # cross_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div[1]/button')))
        # print("Cross button found.")
        # print(cross_button)
        # if cross_button:
        #     click_element(cross_button)

        # Click the final download button if available
        final_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div/article/section[1]/div[1]/div/a')))
        print("Final download button found.")
        click_element(final_button)
        print("Download started.")
        time.sleep(10)
    except Exception as e:
        print(f"An error occurred during download: {e}")

def select_and_download_software():
    """Navigate the software list and initiate downloads."""
    driver.get('https://download.cnet.com/')
    try:
        # Click "See All" to view the full software list
        see_all_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/section[1]/div/div[1]/div/div/div/a')))
        print("See All button found.")
        click_element(see_all_button)

        # Iterate over the first 5 software items and download them
        for i in range(5):
            print(f"Processing software {i + 1}")
            software_link = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div[1]/div/div/div[2]/ul/li[{i+1}]/a/div[1]/div[2]/h2')))
            click_element(software_link)
            download_software()

            # Navigate back to the software list after each download
            driver.get('https://download.cnet.com/security/windows/')
            time.sleep(5)
    except Exception as e:
        print(f"An error occurred while selecting software: {e}")

def main():
    """Main function to start the download process."""
    select_and_download_software()
    input("Press Enter to close the browser...")

if __name__ == "__main__":
    main()
    driver.quit()
