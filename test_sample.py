import pytest
from core import Core

@pytest.mark.usefixtures('init_driver')
class TestSample(Core):
  settings_tab = (AppiumBy.ACCESSIBILITY_ID, 'Settings')
  new_settings = (AppiumBy.ACCESSIBILITY_ID, 'new settings')
  core = Core(self.driver)
  def test_sample(self, get_current_test_name):
      core.click(self..settings_tab)
      core.wait_until_element_visible(self.new_settings)
