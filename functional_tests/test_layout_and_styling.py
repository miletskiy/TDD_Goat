
from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Edith goes to the home page
        # self.browser.get(self.live_server_url)
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)

        # She notices the input box is nicely centered
        # inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width']/2,
            512,
            delta = 5
            )
        # She starts a new list and sees the input is nicely
        # centered there too
        inputbox.send_keys('testing\n')
        inputbox = self.get_item_input_box()
        # inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )
    # def test_css_is_set_correctly(self):
    #     pass
        # self.browser.get('http://localhost:8000/static/bootstrap/css/bootstrap.min.css')

 
    #     # response = self.browser.get('http://localhost:8000/static/bootstrap/css/bootstrap.min.css')
    #     c = Client()
    #     response = c.get('/static/bootstrap/css/bootstrap.min.css')
    #     self.assertEqual(response.status_code, 200) 


    #                     # http://localhost:8000/static/bootstrap/css/bootstrap.min.css
    #     # css_url = self.browser.current_url
    #     # self.assertRegex(francis_list_url, '/lists/.+')
