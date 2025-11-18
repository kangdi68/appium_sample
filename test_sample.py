import pytest

@pytest.mark.usefixtures('init_driver')
class TestSample(Core):
  settings_tab = (AppiumBy.ACCESSIBILITY_ID, 'Settings')
  new_settings = (AppiumBy.ACCESSIBILITY_ID, 'new settings')
  
  def test_sample(self, get_current_test_name):
      self.click(self..settings_tab)
      self.wait_until_element_visible(self.new_settings)
