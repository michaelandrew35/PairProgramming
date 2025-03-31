import unittest
from accountingSystem import AccountingSystem


class TestAccountingSystem(unittest.TestCase):
    """Unit and integration tests for the AccountingSystem"""

    def setUp(self):
        """Prepare a new AccountingSystem instance for testing with known user ID"""
        self.system = AccountingSystem()
        self.validId = "18501179"  # 有多筆資料
        self.invalidId = "notexist"
        self.system.init(self.validId)

    def testTotalExpenses(self):
        """Test if total expenses are calculated correctly for a valid user"""
        # input.txt 中 user 18501179 的總支出：
        # 399 + 229 + 3000 + 357 + 180 + 36 + 128000000 + 4096 + 650 = 128008947
        expectedTotal = 399 + 229 + 3000 + 357 + 180 + 36 + 128000000 + 4096 + 650
        actualTotal = self.system.totalExpenses()
        self.assertEqual(actualTotal, expectedTotal)

    def testDayExpensesWithValidDate(self):
        """Test if specific day's expense is returned correctly"""
        # 2024-04-22 -> 399 + 3000 + 36 = 3435
        self.assertEqual(self.system.dayExpenses("2024-04-22"), 3435)

    def testDayExpensesWithInvalidDate(self):
        """Test if non-existent date returns -1"""
        self.assertEqual(self.system.dayExpenses("2000-01-01"), -1)

    def testMonthExpensesWithValidMonth(self):
        """Test if monthly average expense is calculated correctly"""
        # 2024-04 有五筆支出：399, 3000, 36, 650, 128000000
        total = 399 + 3000 + 36 + 650 + 128000000
        avg = total / 5
        self.assertAlmostEqual(self.system.monthExpenses("2024-04"), avg)

    def testMonthExpensesWithNoTransactions(self):
        """Test if querying an empty month returns -1"""
        self.assertEqual(self.system.monthExpenses("1999-12"), -1)

    def testAllTransactionsOutput(self):
        """Integration test: check if all transactions are printed (mocked with count)"""
        # 檢查交易筆數是否正確（用戶18501179有9筆）
        self.assertEqual(len(self.system.transactions), 9)

    def testInitWithInvalidId(self):
        """Test init function with user ID that has no transactions"""
        system2 = AccountingSystem()
        system2.init(self.invalidId)
        self.assertEqual(len(system2.transactions), 0)

    def testTotalExpensesOnEmptyInit(self):
        """Test totalExpenses when no transactions are found"""
        system2 = AccountingSystem()
        system2.init("00000000")  # 沒有的 ID
        self.assertEqual(system2.totalExpenses(), 0)

    def testExitProgramIsCallable(self):
        """Test that exitprogram method exists and is callable (but not executed)"""
        self.assertTrue(callable(self.system.exitprogram))


if __name__ == '__main__':
    unittest.main()
