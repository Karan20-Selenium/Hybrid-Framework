import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//li[@class='nav-item has-treeview menu-open']//ul[@class='nav nav-treeview']//li[1]//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@href='/Admin/Customer/Create']//i[@class='fas fa-plus-square']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"
    txt_Newsletter_xpath = "// div[@class='card-body']//div[9]//div[2]//div[1][@class='k-multiselect-wrap k-floatwrap']"
    lstitem_Test_Store_2_xpath = "// ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']//li[2]"



    def __init__(self,driver):

        self.driver = driver

    def clickOnCustomersMenu(self):

        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):

        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):

        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):

        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,fname):

        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):

        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setGender(self,gender):

        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdFeMaleGender_id).click()

        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()


    def setDob(self,dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setNewsletter(self):

        self.driver.find_element_by_xpath(self.txt_Newsletter_xpath).click()
        self.driver.find_element_by_xpath(self.lstitem_Test_Store_2_xpath).click()

    def setCustomerRoles(self,role):
        # To delete previously available register
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()

        if role == 'Registered':
            # Here user can be registered(or) Guest, only one

            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)

        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)

        elif role=='Guests':
            self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()

            self.driver.find_element_by_xpath(self.lstitemGuests_xpath).click()

        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)

        else:

            self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()

            self.driver.find_element_by_xpath(self.lstitemGuests_xpath).click()

    # time.sleep(3)
        # #self.listitem.click()
        # self.driver.execute_script("arguments[0].click();",self.listitem)


    def setManagerOfVendor(self,value):

        drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self,content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
























































