import unittest
import string
#symbol: capitalized, 1-7 alpha characters
#chart type: 1 numeric character, 1 or 2
#time series: 1 numeric character, 1 - 4
#start date: date type YYYY-MM-DD
#end date: date type YYYY-MM-DD
def dateFormatter(x):
        dateArray = x.split('-')
        dateArrayReturn = (dateArray[0] + '-' + dateArray[1] + '-' + dateArray[2])
        return dateArrayReturn
def yearChecker(x):
    dateArray = x.split('-')
    yearReturn = dateArray[0]
    return yearReturn
def monthChecker(x):
    dateArray = x.split('-')
    monthReturn = dateArray[1]
    return monthReturn
def dayChecker(x):
    dateArray = x.split('-')
    dayReturn = dateArray[2]
    return dayReturn
class TestProject3(unittest.TestCase):
    
    def setUp(self):
        self.symbol = "GOOGL"
        self.alphaSymbol = (self.symbol).isalpha()
        self.capSymbol = (self.symbol).upper()
        self.chartType = 2
        self.timeSeries = 1
        self.startDate = "2022-10-20"
        self.endDate = "2022-11-20"
    def test_SymbolType(self):
        self.assertIsInstance(self.symbol, str)
        self.assertTrue(self.alphaSymbol)
    def test_SymbolLength(self):
        self.assertLessEqual(len(self.symbol),7)
        self.assertGreaterEqual(len(self.symbol),1)
    def test_SymbolCapital(self):
        self.assertEqual(self.symbol,self.capSymbol)
    def test_ChartType(self):
        self.assertIsInstance(self.chartType, int)
    def test_ChartLength(self):
        self.assertLessEqual(self.chartType,2)
        self.assertGreaterEqual(self.chartType,1)
    def test_SeriesType(self):
        self.assertIsInstance(self.timeSeries, int)
    def test_SeriesLength(self):
        self.assertLessEqual(self.timeSeries,4)
        self.assertGreaterEqual(self.timeSeries,1)
    def test_StartDate(self):
        self.assertEqual(self.startDate, dateFormatter(self.startDate))
    def test_StartDate(self):
        self.assertEqual(self.endDate, dateFormatter(self.endDate))
    def test_yearFormat(self):
        self.assertEqual(len(yearChecker(self.startDate)), 4)
    def test_monthFormat(self):
        self.assertEqual(len(monthChecker(self.startDate)), 2)
    def test_dayFormat(self):
        self.assertEqual(len(dayChecker(self.startDate)), 2)

if __name__ == "__main__":
    unittest.main()