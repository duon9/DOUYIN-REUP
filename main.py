import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import random
import threading


def down_vid(video_url):
    try:
        response = requests.get(video_url)
        if response.status_code == 200:
            local_file_path = generate_random_filename()
            with open(local_file_path, "wb") as local_file:
                local_file.write(response.content)
            print("Download finished")
        else:
            print("Download failed")
    except Exception as e:
        print("Exception:", e)


def get_link(url):
    try:
        options = Options()
        options.add_argument('--disable-infobars')
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path=r"C:\Users\ADMIN\Desktop\video\chromedriver.exe", options=options)
        
        wait = WebDriverWait(driver, 10)
        driver.get(url)
        
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "dy-account-close")))
        container = driver.find_element(By.CLASS_NAME, "xg-video-container")
        video = container.find_element(By.TAG_NAME, "video")
        source = video.find_element(By.TAG_NAME, "source")
        
        link = source.get_attribute("src")
        down_vid(link)
    except Exception as e:
        print("Exception:", e)
    finally:
        driver.quit()


def check_trend(n):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-infobars')
    options.add_argument('--start-maximized')
    # options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=r"C:\Users\ADMIN\Desktop\video\chromedriver.exe", options=options)
    wait = WebDriverWait(driver, 10)
    try:
        driver.get('https://www.douyin.com/')
        action = ActionChains(driver)
        
        remove_banner = driver.find_element(By.CLASS_NAME, 'dy-account-close')
        
        driver.execute_script("arguments[0].click();", remove_banner)
        
        for i in range(n):
            try:
                container = driver.find_element(By.CLASS_NAME, "xg-video-container")
                video = container.find_element(By.TAG_NAME, "video")
                source = video.find_element(By.TAG_NAME, "source")
        
                link = source.get_attribute("src")
                down_vid(link)
                        

                time.sleep(2)
            
                action.send_keys(Keys.ARROW_DOWN).perform()
            except:
                pass
    except Exception as e:
        print("Exception:", e)
    finally:
        driver.quit()
        
def generate_random_filename():
    lst = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','j','k','l','u','i','o','p']
    s = ''
    for i in range(6):
        s += random.choice(lst)
    return s + '.mp4'


def post_to_insta():
    try:
        profile = r"C:\Users\ADMIN\AppData\Local\Google\Chrome\User Data\Profile 13"
        options = webdriver.ChromeOptions()
        options.add_argument("disable-infobars")
        options.add_argument("no-sandbox")
        options.add_argument("disable-extensions")
        options.add_argument("disable-dev-shm-usage")
        options.add_argument("user-data-dir=C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data")
        options.add_argument("profile-directory=Profile 13")
        driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver.exe", options=options)
        
        try:
            driver.get("https://www.instagram.com/")
            time.sleep(200)
        except Exception as e:
            print("Exception:", e)
        finally:
            driver.quit()
    except Exception as e:
        print("Exception:", e)
        
def thread_task(thread_id):
    print(f"Thread {thread_id} executing")
    # Your task code here
    
if __name__ == "__main__":
    threads = []
    n = int(input("ENTER THE NUMBER OF VIDEO: "))
    
    for i in range(n):
        thread = threading.Thread(target=check_trend(n))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
