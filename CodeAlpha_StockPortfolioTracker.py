import requests
API_KEY = '8WQZNYU9S1K179VK'  # Replace we can with actual API key

def get_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'Global Quote' in data:
        return {
            'symbol': data['Global Quote']['01. symbol'],
            'price': float(data['Global Quote']['05. price']),
            'change_percent': float(data['Global Quote']['10. change percent'].strip('%'))
        }
    else:
        return None
class Portfolio:                #we create a class for portofolio
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):          #add stock   
        if symbol in self.stocks:
            self.stocks[symbol] += quantity
        else:
            self.stocks[symbol] = quantity

    def remove_stock(self, symbol, quantity):          #remove stocks
        if symbol in self.stocks:
            self.stocks[symbol] -= quantity
            if self.stocks[symbol] <= 0:
                del self.stocks[symbol]

    def get_portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.stocks.items():
            stock_data = get_stock_data(symbol)
            if stock_data:
                total_value += stock_data['price'] * quantity
        return total_value
def main():
    portfolio = Portfolio()

    while True:                                             
        print("\n1. Add the stock to portfolio")
        print("2. Remove the stock from portfolio")
        print("3. View the portfolio value")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter the stock symbol: ")
            quantity = int(input("Enter the quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter the stock symbol: ")
            quantity = int(input("Enter the quantity: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            value = portfolio.get_portfolio_value()
            print(f"Portfolio value: ${value:.2f}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()