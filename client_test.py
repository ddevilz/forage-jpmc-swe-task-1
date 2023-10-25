import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      expected_stock = quote['stock']
      expected_bid_price = float(quote['top_bid']['price'])
      expected_ask_price = float(quote['top_ask']['price'])
      expected_price = (expected_bid_price + expected_ask_price) / 2
      result = getDataPoint(quote)
      self.assertEqual(result, (expected_stock, expected_bid_price, expected_ask_price, expected_price))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # for i in quotes:
    #    self.assertEqual(getDataPoint(i), (i['stock'], i['bid_price'], i['ask_price'],(i['bid_price'] + i['ask_price']/2)))
    for quote in quotes:
      expected_stock = quote['stock']
      expected_bid_price = float(quote['top_bid']['price'])
      expected_ask_price = float(quote['top_ask']['price'])
      expected_price = (expected_bid_price + expected_ask_price) / 2
      result = getDataPoint(quote)
      self.assertEqual(result, (expected_stock, expected_bid_price, expected_ask_price, expected_price))

  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
