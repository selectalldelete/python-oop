class Apple: # Base class
    manufacturer = "Apple Inc."
    contact_website = "www.apple.com/contact"

    def contact_details(self):
        print('To contact us, log on to', self.contact_website)

class MacBook(Apple): # Derived class
    def __init__(self):
        self.year_of_manufacture = '2017'

    def manufacture_details(self):
        print('This MacBook was manufactured in the year {} by {}'.format(
            self.year_of_manufacture, self.manufacturer))


macbook = MacBook()
macbook.manufacture_details()
macbook.contact_details()
