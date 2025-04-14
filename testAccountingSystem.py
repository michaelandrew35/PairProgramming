import unittest
from accountingSystem import AccountingSystem


class TestAccountingSystem(unittest.TestCase):
    """Unit and integration tests for the AccountingSystem"""

    def setUp(self):
        """
        Setup for each test case:
            - Initializes AccountingSystem
            - Uses test user ID 18501179
        """
        self.system = AccountingSystem()
        self.validId = "18501179"
        self.invalidId = "notexist"
        self.system.init(self.validId)

    def testInitWithInvalidId(self):
        """
        Test function: AccountingSystem.init()
        Test description:
            Initialize with a user ID that doesn't exist (e.g., 'notexist')
            and check that no transactions are loaded.
        """
        system2 = AccountingSystem()
        system2.init(self.invalidId)
        self.assertEqual(len(system2.transactions), 0)

    def testTotalExpenses(self):
        """
        Test function: AccountingSystem.totalExpenses()
        Test description:
            Given user ID 18501179, test if the total of 9 transaction amounts is correctly calculated 
            as (399 + 229 + 3000 + 357 + 180 + 36 + 128000000 + 4096 + 650) = 128008947.  
        """
        expectedTotal = 128008947
        actualTotal = self.system.totalExpenses()
        self.assertEqual(actualTotal, expectedTotal)

    def testTotalExpensesOnEmptyInit(self):
        """
        Test function: AccountingSystem.totalExpenses()
        Test description:
            If no transactions exist (e.g., from ID '00000000'),
            totalExpenses should return 0.
        """
        system2 = AccountingSystem()
        system2.init("00000000")
        self.assertEqual(system2.totalExpenses(), 0)

    def testDayExpensesWithValidDate(self):
        """
        Test function: AccountingSystem.dayExpenses()
        Test description:
            For date '2024-04-22', test if the total expenses
            399 + 3000 + 36 = 3435 is returned correctly.
        """
        self.assertEqual(self.system.dayExpenses("2024-04-22"), 3435)

    def testDayExpensesWithInvalidDate(self):
        """
        Test function: AccountingSystem.dayExpenses()
        Test description:
            For a date with no transactions like '2000-01-01',
            the function should return -1.
        """
        self.assertEqual(self.system.dayExpenses("2000-01-01"), -1)

    def testMonthExpensesWithValidMonth(self):
        """
        Test function: AccountingSystem.monthExpenses()
        Test description:
            For '2024-04', user has 5 expenses: 399, 3000, 36, 650, 128000000.
            Should return average over 30 days (April): total / 30
        """
        total = 399 + 3000 + 36 + 650 + 128000000
        avg = total / 30
        self.assertAlmostEqual(self.system.monthExpenses("2024-04"), avg)

    def testMonthExpensesWithNoTransactions(self):
        """
        Test function: AccountingSystem.monthExpenses()
        Test description:
            For month '1999-12', with no transactions,
            the function should return -1.
        """
        self.assertEqual(self.system.monthExpenses("1999-12"), -1)

    def testAllTransactionsOutput(self):
        """
        Test function: AccountingSystem.allTransactions()
        Test description:
            Verifies that the system reads exactly 9 transactions
            for user 18501179 from input.txt.
        """
        self.assertEqual(len(self.system.transactions), 9)

    def testExitProgramIsCallable(self):
        """
        Test function: AccountingSystem.exitprogram()
        Test description:
            Check that the exitprogram() method exists and is callable
            (do not actually execute it during test).
        """
        self.assertTrue(callable(self.system.exitprogram))

    def testIntegrationValidUser(self):
        """
        Test function: Full integration test for valid user 17111563
        Test description:
            This test initializes user 17111563 and tests:
            - totalExpenses(): should return the sum of all their expenses
            - allTransactions(): should print without crashing
            - dayExpenses(): should return correct sum for specific day
            - monthExpenses(): should return correct monthly average
            - exitprogram(): should be callable
        """
        system = AccountingSystem()
        system.init("17111563")
        expectedTotal = 87 + 215 + 1000000 + 123 + 449 + 20 + 999 + 102 + 875 + 125
        self.assertEqual(system.totalExpenses(), expectedTotal)
        self.assertEqual(system.dayExpenses("2023-01-02"), 338)  # 215 + 123
        self.assertEqual(system.dayExpenses("2000-01-01"), -1)
        jan_total = 87 + 215 + 123 + 449 + 20 + 999 + 875 + 125
        self.assertAlmostEqual(system.monthExpenses("2023-01"), jan_total / 31)
        self.assertEqual(system.monthExpenses("1999-12"), -1)
        try:
            system.allTransactions()
            success = True
        except Exception:
            success = False
        self.assertTrue(success)
        self.assertTrue(callable(system.exitprogram))

    def testIntegrationInvalidUser(self):
        """
        Test function: Full integration test for invalid user 99999999
        Test description:
            This test verifies system behavior when initializing with a non-existent user ID.
            All feature methods should return -1 or execute without error.
        """
        system = AccountingSystem()
        system.init("99999999")
        self.assertEqual(system.totalExpenses(), 0)
        self.assertEqual(system.dayExpenses("2024-01-01"), -1)
        self.assertEqual(system.monthExpenses("2024-01"), -1)
        try:
            system.allTransactions()
            success = True
        except Exception:
            success = False
        self.assertTrue(success)
        self.assertTrue(callable(system.exitprogram))


if __name__ == '__main__':
    unittest.main()
