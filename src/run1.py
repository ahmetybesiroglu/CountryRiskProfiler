import json
import atexit
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.knowyourcountry.com/country-reports/')

# Function to map color codes to names
def map_color(color_code):
    color_map = {
        'rgb(204, 50, 50)': 'red',
        'rgb(45, 201, 55)': 'green',
        'rgb(231, 180, 22)': 'yellow'
    }
    return color_map.get(color_code, 'unknown')

# List to hold the extracted data
country_data = []

# Function to save data to a JSON file
def save_data(data, filename="country_data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

# Register the save_data function to be called upon program exit
atexit.register(save_data, country_data)

# Wait for the page to load


# Get the container with all country cards
container = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div/div[2]/div')

# Find all country cards
country_cards = container.find_elements(By.CLASS_NAME, 'country-card-grid-item')

# Iterate over each country card
for index, card in enumerate(country_cards):
    try:
        # Scroll to the country card to ensure visibility
        actions = ActionChains(driver)
        actions.move_to_element(card).perform()
        
        # Extract the country name
        country_name = card.find_element(By.CLASS_NAME, 'name').text

        # Click on the 'View Report' button
        view_report_button = card.find_element(By.CLASS_NAME, 'button')
        view_report_button.click()
        
        # Wait for the report page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'score-and-rating'))
        )
        
        # Extract country rating
        rating_element = driver.find_element(By.CLASS_NAME, 'score-and-rating')
        rating = rating_element.find_element(By.TAG_NAME, 'b').text
        
        # Extract details (color and title only)
        details = driver.find_elements(By.CLASS_NAME, 'country-report-detail')
        detail_list = []
        for detail in details:
            color_style = detail.find_element(By.CLASS_NAME, 'detail-color').get_attribute('style')
            color_code = color_style.split('background-color: ')[1].strip(';')
            detail_color = map_color(color_code)
            detail_title = detail.find_element(By.TAG_NAME, 'h5').text
            detail_list.append({'title': detail_title, 'color': detail_color})
        
        # Add the data to the list
        country_data.append({'country_name': country_name, 'rating': rating, 'details': detail_list})
        
        # Print debugging information
        print(f"Scraped data for {country_name}: rating {rating}")
        print(f"Details: {detail_list}\n")

        # Save progress every 5 countries
        if (index + 1) % 5 == 0:
            save_data(country_data)

        # Navigate back to the main country reports page
        driver.back()
        
        # Wait for the main page to load

        
        # Re-fetch the container and country cards
        container = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div/div[2]/div')
        country_cards = container.find_elements(By.CLASS_NAME, 'country-card-grid-item')
        
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.back()
        container = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div/div[2]/div')
        country_cards = container.find_elements(By.CLASS_NAME, 'country-card-grid-item')

# Final save of data after completing the loop
save_data(country_data)

# Close the driver
driver.quit()
