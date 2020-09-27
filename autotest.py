#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import HTMLTestRunner
import time

class TestDemo(unittest.TestCase):
    """测试用例"""

    def setUp(self):
        print('========== begin ==========')

    def test_success(self):
        self.assertEqual(1 + 1, 2)

    def test_fail(self):
        self.assertEqual(1 + 1, 10)

    def test_error(self):
        self.assertEqual(x, 1024)

    def tearDown(self):
        print('========== end ==========')

if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()

    # 添加测试用例
    suite.addTest(TestDemo("test_success"))
    suite.addTest(TestDemo("test_fail"))
    suite.addTest(TestDemo("test_error"))

    # 报告路径
    date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    report_abspath = 'report_' + date_time + '.html'
    
    # 执行测试
    with open(report_abspath, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='TestDemo unit test',
            description='TestDemo report output by HTMLTestRunner.'
        )
        runner.run(suite)
