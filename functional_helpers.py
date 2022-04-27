def user_login(driver, user_email, user_password):
    """ Login user to website using given email and password

    :param driver: webdriver instance
    :param user_email: user email
    :param user_password: user password
    :return: None
    """
    # finding login input box and sending value
    login_input_element = driver.find_element_by_xpath('//*[@type="email"]')
    login_input_element.send_keys(user_email)
    # finding password input box and sending value
    login_input_element = driver.find_element_by_xpath('//*[@type="password"]')
    login_input_element.send_keys(user_password)
    # finding button 'sign in'
    button_next_element = driver.find_element_by_xpath('//*[@id="submit-login"]')
    button_next_element.click()


def get_title(driver, url):
    driver.get(url)
    return driver.title


def assert_title(class_obj, driver, expected_title, url):
    actual_title = get_title(driver, url)
    class_obj.assertEqual(expected_title, actual_title,
                        f"Title on page {driver.current_url} differ from the expected one")
