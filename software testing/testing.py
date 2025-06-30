import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class StudentManagementTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("file:///absolute/path/to/index.html")  # UPDATE path
        cls.driver.maximize_window()
        time.sleep(1)

    def test_1_title(self):
        self.assertIn("Student Management System", self.driver.title)

    def test_2_open_enrollment_form(self):
        self.driver.find_element(By.ID, "btnEnroll").click()
        time.sleep(1)
        form = self.driver.find_element(By.ID, "enrollmentForm")
        self.assertTrue(form.is_displayed())

    def test_3_enroll_student(self):
        d = self.driver
        d.find_element(By.ID, "name").send_keys("John")
        d.find_element(By.ID, "fatherName").send_keys("Smith")
        d.find_element(By.ID, "dob").send_keys("2002-05-20")
        d.find_element(By.ID, "gender").send_keys("Male")
        d.find_element(By.ID, "bloodGroup").send_keys("A+")
        d.find_element(By.ID, "address").send_keys("123 Street")
        d.find_element(By.ID, "email").send_keys("john@example.com")
        d.find_element(By.ID, "contact").send_keys("9876543210")
        d.find_element(By.ID, "enrollBtn").click()
        time.sleep(1)

    def test_4_student_appears_in_list(self):
        self.driver.find_element(By.ID, "btnList").click()
        time.sleep(1)
        table = self.driver.find_element(By.ID, "studentsTable")
        self.assertIn("John", table.text)

    def test_5_update_grade(self):
        self.driver.find_element(By.ID, "btnGrades").click()
        time.sleep(1)
        input_box = self.driver.find_element(By.CSS_SELECTOR, "#gradesTable tbody tr:first-child td:nth-child(2) input")
        input_box.clear()
        input_box.send_keys("A")
        self.driver.find_element(By.CSS_SELECTOR, "#gradesTable tbody tr:first-child td:nth-child(3) button").click()
        time.sleep(1)

    def test_6_search_existing_student(self):
        self.driver.find_element(By.ID, "searchBox").clear()
        self.driver.find_element(By.ID, "searchBox").send_keys("John")
        time.sleep(1)
        table = self.driver.find_element(By.ID, "studentsTable")
        self.assertIn("John", table.text)

    def test_7_search_non_existing_student(self):
        self.driver.find_element(By.ID, "searchBox").clear()
        self.driver.find_element(By.ID, "searchBox").send_keys("NonExistent")
        time.sleep(1)
        table = self.driver.find_element(By.ID, "studentsTable")
        self.assertNotIn("NonExistent", table.text)

    def test_8_empty_form_submission(self):
        self.driver.find_element(By.ID, "btnEnroll").click()
        self.driver.find_element(By.ID, "enrollmentForm").reset()
        self.driver.find_element(By.ID, "enrollBtn").click()
        time.sleep(1)
        # Form doesn't submit due to required fields
        self.assertTrue(self.driver.find_element(By.ID, "enrollment").is_displayed())

    def test_9_navigation_buttons(self):
        self.driver.find_element(By.ID, "btnGrades").click()
        time.sleep(1)
        self.assertTrue(self.driver.find_element(By.ID, "grades").is_displayed())

        self.driver.find_element(By.ID, "btnMessages").click()
        time.sleep(1)
        self.assertTrue(self.driver.find_element(By.ID, "communication").is_displayed())

    def test_10_message_send_fields_exist(self):
        self.driver.find_element(By.ID, "btnMessages").click()
        time.sleep(1)
        self.assertTrue(self.driver.find_element(By.ID, "recipientEmail").is_displayed())
        self.assertTrue(self.driver.find_element(By.ID, "messageInput").is_displayed())

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()