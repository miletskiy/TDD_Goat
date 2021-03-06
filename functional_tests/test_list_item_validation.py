
# from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    # @skip
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        # self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank.
        # error = self.browser.find_element_by_css_selector('.has-error')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item, blin")

        # She tries again with some text for the  item, which now works
        self.get_item_input_box().send_keys('Buy one bottle of milk\n')
        # self.browser.find_element_by_id('id_new_item').send_keys('Buy one bottle of milk\n')
        self.check_for_row_in_list_table('1: Buy one bottle of milk')

        # Perversely, she now decides to submit a second blank list item
        self.get_item_input_box().send_keys('\n')
        # self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy one bottle of milk')
        # error = self.browser.find_element_by_css_selector('.has-error')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item, blin")

        # And she can correct it by filling some text in
        self.get_item_input_box().send_keys('Make cup of tea\n')
        # self.browser.find_element_by_id('id_new_item').send_keys('Make cup of tea\n')
        self.check_for_row_in_list_table('1: Buy one bottle of milk')
        self.check_for_row_in_list_table('2: Make cup of tea')

        # self.fail('write me!')

    def test_cannot_add_duplicate_items(self):
        # Edith goes to the home page and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        # She accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies\n')

        # She sees a helpful error message
        self.check_for_row_in_list_table('1: Buy wellies')
        # error = self.browser.find_element_by_css_selector('.has-error')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")

    def test_error_messages_are_cleared_on_input(self):
        # Edith starts a new list in a way that causes a validation error:
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        # error = self.browser.find_element_by_css_selector('.has-error')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # She starts typing in the input box to clear the error
        self.get_item_input_box().send_keys('a')

        # She is pleased to see that the error message disappears
        # error = self.browser.find_element_by_css_selector('.has-error')
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())



# if __name__ == '__main__':
#     unittest.main(warnings='ignore')

