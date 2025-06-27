import datetime
import yfinance as yf
import plotly.graph_objects as go
import webbrowser
import plotly.io as pio

pio.renderers.default = "browser"  # This line ensures fig.show() opens in your browser

current_time = datetime.datetime.now()

total_stock_values = []
stock_names = []

class stock_protfolio():
    def get_stock_value(interval='15m'):
        global num_stocks
        num_stocks = int(input("hey how many stocks do you have ??"))
        for i in range(num_stocks):
            stock_name = input("stock symbol: ").strip().upper()
            stock_names.append(stock_name)

            data = yf.download(tickers=stock_name, period='1d', interval=interval)
            if data.empty or 'Open' not in data.columns:
                print("No data found for", stock_name)
                total_stock_values.append(0)
                continue

            now_value = data['Open'].iloc[-1]

            num_shares = input('how many shares do you have?? ')
            total_val = now_value * float(num_shares)
            total_val = float('%.2f' % total_val)
            total_stock_values.append(total_val)

            print("Value of " + stock_name + " is " + str(now_value))
            print("Total value of shares: " + str(total_val))

    def create_pie_chart():
        total = 0
        labels = stock_names
        values = total_stock_values

        for i in range(len(total_stock_values)):
            total += total_stock_values[i]

        fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent', insidetextorientation='radial')])
        fig.update_layout(title_text="stock portfolio: $ " + str(float('%.2f' % total)))

        print(current_time.strftime('%Y-%m-%d'))
        print(total_stock_values)
        print(stock_names)
        fig.show()

    if __name__ == "__main__":
        get_stock_value()
        create_pie_chart()
