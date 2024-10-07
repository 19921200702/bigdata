# from unittest import TestCase
from unittest import TestCase

from 测试1.util.mysql_util import MySQLUtil


class TestMySQLUtil(TestCase):
    def setUp(self) -> None:
        self.db_util = MySQLUtil()
    def test_query(self):
        self.db_util.execute('show databases;')



