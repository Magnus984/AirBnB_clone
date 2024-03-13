#!/usr/bin/python3
import unittest
from models import BaseModel


class TestBase_model_instatiation(unittest.TestCase):
    """Unittests for testing instantiation of the base class."""

    def test_uuid_arg(self):
        b1 = BaseModel()
        self.assertIsInstance(b.id, string)


class TestBase_model_methods(unittest.TestCase):
    def test_save(self):
        s1 = BaseModel()
        before_save = s1.updated_time
        s1.save()
        after_save = s1.updated_time
        self.assertNotEqual(before_save, after_save)

    def test_to_dict(self):
        s1 = BaseModel()
        cp = s1.to_dict()
        self.assertEqual(set(cp.keys()), set(s1.__dict__.keys()))
