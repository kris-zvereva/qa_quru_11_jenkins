import os

from selene import browser, have, command

REGISTRATION_PAGE_URL = '/automation-practice-form'
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(CURRENT_DIR, '..', '..', 'resources', 'test_image.png')

class RegistrationPage:
    def __init__(self):
        self.url = REGISTRATION_PAGE_URL
        self.file_path = os.path.abspath(IMAGE_PATH)
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.phone_input = browser.element('#userNumber')
        self.state = browser.element('#state')


    def open(self):
        browser.open(self.url)
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, first_name):
        self.first_name.type(first_name)

    def fill_last_name(self, last_name):
        self.last_name.type(last_name)

    def fill_email(self, email):
        self.email.type(email)

    def select_gender(self, gender):
        gender_map = {'Male': '1', 'Female': '2', 'Other': '3'}
        browser.element(f'label[for="gender-radio-{gender_map[gender]}"]').click()

    def fill_phone(self, phone):
        self.phone_input.type(phone)

    def fill_dob(self, day, month, year):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('[class="react-datepicker__month-select"]').click()
        browser.element(f'.//option[@value={month}]').click()
        browser.element('[class="react-datepicker__year-select"]').click()
        browser.element(f'[value="{year}"]').click()
        browser.element(f'[class="react-datepicker__day react-datepicker__day--00{day}"]').click()

    def select_hobbies(self, *hobbies):
        hobby_map = {'Sports': '1', 'Reading': '2', 'Music': '3'}
        for hobby in hobbies:
            browser.element(f'label[for="hobbies-checkbox-{hobby_map[hobby]}"]').click()

    def fill_subjects(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def upload_image(self):
        browser.element('#uploadPicture').send_keys(self.file_path)

    def fill_address(self, text_address):
        browser.element('#currentAddress').type(text_address)

    def fill_state_and_city(self, state, city):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()
        browser.element('#city').click()
        browser.element('#react-select-4-input').type(city).press_enter()

    def submit(self):
        browser.element('#submit').click()

    def should_have_modal_text(self, text):
        browser.element('#example-modal-sizes-title-lg').should(have.text(text))

    def should_have_registered(self, *expected_rows):
        expected_texts = ['Label Values']
        for label, value in expected_rows:
            expected_texts.append(f'{label} {value}')
        browser.all('tr').should(have.texts(*expected_texts))
