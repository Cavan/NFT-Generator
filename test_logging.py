from app_logging import AppLogger
import unittest


class TestAppLogging(unittest.TestCase):
    
   
    def setUp(self):
        self.appLogger = AppLogger()
        

    def tearDown(self):
        pass
    
    def test_log_info(self):
        self.assertTrue(self.appLogger.log_info("TEST: Logging Info"))
    
    def test_log_warning(self):
        self.assertTrue(self.appLogger.log_warnings("TEST: Logging Warning"))
    
    def test_log_error(self):
        self.assertTrue(self.appLogger.log_errors("TEST: Logging Error"))
    
    # def test_log_exception(self):
    #     self.assertTrue(self.appLogger.log_exceptions("TEST: Logging Exception"))
    
    
if __name__ == '__main__':
    unittest.main()