        this code is not working anymore
        
        modal = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
