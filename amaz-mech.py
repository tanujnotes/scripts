import mechanize
URL = 'https://goo.gl/DPDz9R' # amazon.in login page
EMAIL = 'your_email@example.com'
PASS = 'your_password'
#Link of the product that we are going to order
PRODUCT = 'http://www.amazon.in/HP-V210W-16GB-USB-Drive/dp/B005LTPPBO/'
#Creating a browser object
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
#Open login page and inspect
response = br.open(URL)
#Print forms on URL. Not important, you can comment out this loop.
for form in br.forms():
    print "Form name:", form.name
    print form
    print
#Select form by name - "signIn"
br.select_form("signIn")
#Login: Fill 'controls' in 'signIn' form
br.form['email'] = EMAIL
br.form['password'] = PASS
br.method = "POST"
response = br.submit()
print response.geturl()
#Uncomment following two lines to check if you are logged in
#logincheck = response.read()
#print logincheck
print "++++++ LOGGED IN ++++++"
response = br.open(PRODUCT)
print response.geturl()
#Forms are arranged as a list data-type. You can select them using index number.
br.select_form(nr = 1)
req = br.click("submit.buy-now")
response = br.open(req)
print "++++++ PRODUCT ++++++"
print response.geturl()
print "++++++ SELECTING COD & CONTINUE ++++++"
br.form = list(br.forms())[0] # Selecting form using index number of list.
#Selecting payment method.
br.form['paymentMethod'] = ['cashOnDeliveryCash']
#Selecting Continue control using its value because name wasn't availble.
for control in br.form.controls:
    if control.value == 'Continue':
        #print control
        #print control.name
        req1 = br.click(control.name)
        print req1
        response1 = br.open(req1)
print "++++++ PLACE ORDER ++++++"
br.select_form('spc') # Selecting form by name
order = br.click("placeYourOrder1") # Selecting control by name
response2 = br.open(order)
