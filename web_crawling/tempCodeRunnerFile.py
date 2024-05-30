        for i in range(11):
            try:
                driver.find_element(By.XPATH, f'//*[@id="newbg_body"]/div[3]/ul/li[{i}]').click()
            except Exception as e:
                print(f'Error at index {i}: {e}')
                