import allure

from model.pages.registration_page import RegistrationPage

@allure.title('Submit practice registration form with valid data')
@allure.description('This test verifies that the practice registration form can be successfully submitted with all required fields filled in and displays correct data in the confirmation modal')
@allure.feature('Registration Form')
@allure.story('Form Submission')
@allure.severity(allure.severity_level.CRITICAL)
def test_submit_practice_form(set_browser):
    with allure.step('open registration form'):
        registration_page = RegistrationPage()
        registration_page.open()

    with allure.step('fill in personal information'):
        registration_page.fill_first_name('First Name')
        registration_page.fill_last_name('Last Name')
        registration_page.fill_email('email@test.qa')
        registration_page.select_gender('Female')
        registration_page.fill_phone('1234567890')

    with allure.step('fill in Date of birth'):
        registration_page.fill_dob(1, 8, 1999)

    with allure.step('fill in hobbies and subjects'):
        registration_page.select_hobbies('Reading')
        registration_page.fill_subjects('Maths')

    with allure.step('upload the image'):
        registration_page.upload_image()

    with allure.step('fill in the address'):
        registration_page.fill_address('test address')
        registration_page.fill_state_and_city('Haryana', 'Karnal')

    with allure.step('submit the form'):
        registration_page.submit()

    with allure.step('check form results'):
        registration_page.should_have_modal_text('Thanks for submitting the form')
        registration_page.should_have_registered(
            ('Student Name', 'First Name Last Name'),
            ('Student Email', 'email@test.qa'),
            ('Gender', 'Female'),
            ('Mobile', '1234567890'),
            ('Date of Birth', '01 September,1999'),
            ('Subjects', 'Maths'),
            ('Hobbies', 'Reading'),
            ('Picture', 'test_image.png'),
            ('Address', 'test address'),
            ('State and City', 'Haryana Karnal')
        )