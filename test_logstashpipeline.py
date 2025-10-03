# test_logstashpipeline.py
"""
Tests for LogstashPipeline module.
"""

import unittest
from logstashpipeline import LogstashPipeline

class TestLogstashPipeline(unittest.TestCase):
    """Test cases for LogstashPipeline class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LogstashPipeline()
        self.assertIsInstance(instance, LogstashPipeline)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LogstashPipeline()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
