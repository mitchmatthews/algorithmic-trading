import quantstats as qs


qs.extend_pandas()

index = {"SPY": 1.3, "BND": -.3}
portfolio = qs.utils.make_index({"SPY": 1.3, "BND": -0.3}, rebalance="1ME", period="5y")

# Debugging: Print the index dictionary
#print("Index dictionary:", index)

try:
    portfolio = qs.utils.make_index(index, period='5y')
    # Debugging: Print the portfolio head
    print("Portfolio head:\n", portfolio.head())
except Exception as e:
    print(f"Error creating portfolio: {e}")

portfolio = qs.utils.make_index(index, period='5y')
portfolio.index = portfolio.index.tz_localize(None)
portfolio.plot_earnings(start_balance= 10000, savefig="output/portfolio_earnings.png")
portfolio.plot_monthly_heatmap(savefig="output/portfolio_heat.png")
#print(portfolio.head())