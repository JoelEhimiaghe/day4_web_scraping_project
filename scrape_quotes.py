Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 ... import json
...
... driver = webdriver.Chrome()
... driver.get("http://quotes.toscrape.com")
...
... all_quotes = []
...
... while True:visibility_of_all_elements_located((By.CLASS_NAME, "quote
...     quotes_elements = WebDriverWait(driver, 10).until(
...         EC.visibility_of_all_elements_located((By.CLASS_NAME, "quote"))     for q in quotes_elements:                                       ...    )                                                               ...     for q in quotes_elements:nt(By.CLASS_NAME, "author").text       ...    text = q.find_element(By.CLASS_NAME, "text").textr})        ...         author = q.find_element(By.CLASS_NAME, "author").text       ...all_quotes.append({"quote": text, "author": author})        ...                                                                     ...     try:                                                        ...         next_button = driver.find_element(By.CSS_SELECTOR, "li.next > a")       sleep(1)                                                    ...         next_button.click()                                         ...         sleep(1)                                                ...     except:                                                         ...         break                                            ...                                                                     ... driver.quit()                                        ...                                                                     ... df = pd.DataFrame(all_quotes)=False)                                ... df.to_csv("quotes.csv", index=False)se)
... df.to_excel("quotes.xlsx", index=False)
...
... with open("quotes.json", "w", encoding="utf-8") as f:nt=4)
...     json.dump(all_quotes, f, ensure_ascii=False, indent=4)
... print("Scraping complete. Data saved to CSV, Excel, and JSON!")
Scraping complete. Data saved to CSV, Excel, and JSON!
...         EC.visibility_of_all_elements_located((By.CLASS_NAME, "e"))
...     quotes_elements = WebDriverWait(driver, 10).until(         ...     )        EC.visibility_of_all_elements_located((By.CLASS_NAME, "quote
...     for q in quotes_elements:
...         text = q.find_element(By.CLASS_NAME, "text").text           ...         author = q.find_element(By.CLASS_NAME, "author").text       ...        all_quotes.append({"quote": text, "author": author})t       ...                                                                     ...try:                                                            ...         next_button = driver.find_element(By.CSS_SELECTOR, "li.next\...     try:next_button = driver.find_element(By.CSS_SELECTOR, "li.next\...         next_button = driver.find_element(By.CSS_SELECTOR, "li.next > a")       sleep(1)                                                    ...         next_button.click()                                         ...         sleep(1)                                                    ...     except:                                                         ...         break                                                ...                                                                     ... driver.quit()                                            ...                                                                     ... df = pd.DataFrame(all_quotes)                                       ...                                                                     ... date_str = datetime.now().strftime("%Y%m%d")  # format: YYYYMMDD    ... csv_file = f"quotes_{date_str}.csv"                                 ... excel_file = f"quotes_{date_str}.xlsx"                              ... json_file = f"quotes_{date_str}.json"                               ...                            ... df.to_csv(csv_file, index=False)                                    ... df.to_excel(excel_file, index=False)                        ...
... with open(json_file, "w", encoding="utf-8") as f:indent=4)
...     json.dump(all_quotes, f, ensure_ascii=False, indent=4)
...
... print(f"Scraping complete. Files saved as:\n{csv_file}\n{excel_file}\n{json_file}")
Scraping complete. Files saved as:
quotes_20251121.csv
quotes_20251121.xlsx
quotes_20251121.json
>>>
... from datetime import datetime
... import os
...
... driver.get("http://quotes.toscrape.com")
...
... all_quotes = []
... while True:                                                    ...
hile True:  EC.visibility_of_all_elements_located((By.CLASS_NAME, "... while True:otes_elements = WebDriverWait(driver, 10).until(exttext
...     quotes_elements = WebDriverWait(driver, 10).until(S_NAME, "quot\
...         EC.visibility_of_all_elements_located((By.CLASS_NAME, "quot\
...         EC.visibility_of_all_elements_located((By.CLASS_NAME, "e")) e"))                                                                    ...    )or q in quotes_elements:(By.CLASS_NAME, "text").texttext
...     for q in quotes_elements:(By.CLASS_NAME, "text").texttext       ...         author = q.find_element(By.CLASS_NAME, "author").text       ...        all_quotes.append({"quote": text, "author": author})        ...                                                                     ...try:                                                            ...         next_button = driver.find_element(By.CSS_SELECTOR, "li.next\
> a")       next_button.click()
> a")       next_button.click()                                         > a")       next_button.click()                                         ...        next_button.click()                                         ...         sleep(1)
...     except:                                                         ...         break                                                       ...                                                                    ... driver.quit()                                                       ... df = pd.DataFrame(all_quotes)                                       ... df = pd.DataFrame(all_quotes)
... date_str = datetime.now().strftime("%Y%m%d")  # format: YYYYMMDDnts\
... date_str = datetime.now().strftime("%Y%m%d")  # format: YYYYMMDDnts\
... documents_folder = os.path.join(os.path.expanduser("~"), "Documents\)  # user's Documents folder                                           ")  # user's Documents folder                                           ")  # user's Documents folder                                            ...                                                                ... csv_file = os.path.join(documents_folder, f"quotes_{date_str}.csv")\... excel_file = os.path.join(documents_folder, f"quotes_{date_str}.xls\"). json_file = os.path.join(documents_folder, f"quotes_{date_str}.jsonx"). json_file =os.path.join(documents_folder, f"quotes_{date_str}.jsonx"). json_file = os.path.join(documents_folder, f"quotes_{date_str}.json\... json_file = os.path.join(documents_folder, f"quotes_{date_str}.json\...     json.dump(all_quotes, f, ensure_ascii=False, indent=4)      ")                                           .")  ...                                                                 ...                                       ... d... print(f"Scraping complete. Files saved in Documents folder:\n{csv_file}\n{excel_file}\n{json_file}")
Traceback (most recent call last):
  File "<python-input-7>", line 17, in <module>
    quotes_elements = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "quote"))
    )
  File "C:\Users\JUMGR-0391\AppData\Local\Programs\Python\Python313\Lib\site-packages\selenium\webdriver\support\wait.py", line 138, in until
    raise TimeoutException(message, screen, stacktrace)
... from datetime import datetime
... import os
...
... driver.get("http://quotes.toscrape.com")
...
... all_quotes = []
... while True:                                                    ...
hile True:  EC.visibility_of_all_elements_located((By.CLASS_NAME, "... while True:otes_elements = WebDriverWait(driver, 10).until(exttext
...     quotes_elements = WebDriverWait(driver, 10).until(S_NAME, "quot\
...         EC.visibility_of_all_elements_located((By.CLASS_NAME, "quot\
...         EC.visibility_of_all_elements_located((By.CLASS_NAME, "e")) e"))                                                                    ...    )or q in quotes_elements:(By.CLASS_NAME, "text").texttext
...     for q in quotes_elements:(By.CLASS_NAME, "text").texttext       ...         author = q.find_element(By.CLASS_NAME, "author").text       ...        all_quotes.append({"quote": text, "author": author})        ...                                                                     ...try:                                                            ...         next_button = driver.find_element(By.CSS_SELECTOR, "li.next\
> a")       next_button.click()
> a")       next_button.click()                                         > a")       next_button.click()                                         ...        next_button.click()                                         ...         sleep(1)
...     except:                                                         ...         break                                                       ...                                                                    ... driver.quit()                                                       ... df = pd.DataFrame(all_quotes)                                       ... df = pd.DataFrame(all_quotes)
... date_str = datetime.now().strftime("%Y%m%d")  # format: YYYYMMDDnts\
... date_str = datetime.now().strftime("%Y%m%d")  # format: YYYYMMDDnts\
... documents_folder = os.path.join(os.path.expanduser("~"), "Documents\)  # user's Documents folder                                           ")  # user's Documents folder                                           ")  # user's Documents folder                                            ...                                                                ... csv_file = os.path.join(documents_folder, f"quotes_{date_str}.csv")\... excel_file = os.path.join(documents_folder, f"quotes_{date_str}.xls\"). json_file = os.path.join(documents_folder, f"quotes_{date_str}.jsonx"). json_file =os.path.join(documents_folder, f"quotes_{date_str}.jsonx"). json_file = os.path.join(documents_folder, f"quotes_{date_str}.json\... json_file = os.path.join(documents_folder, f"quotes_{date_str}.json\...     json.dump(all_quotes, f, ensure_ascii=False, indent=4)      ")                                           .")  ...                                                                 ...                                       ... d... print(f"Scraping complete. Files saved in Documents folder:\n{csv_file}\n{excel_file}\n{json_file}")
Scraping complete. Files saved in Documents folder:
C:\Users\JUMGR-0391\Documents\quotes_20251121.csv
C:\Users\JUMGR-0391\Documents\quotes_20251121.xlsx
C:\Users\JUMGR-0391\Documents\quotes_20251121.json
>>>
