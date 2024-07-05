
class SharpeRatio():
    def __init__(cls, stock_returns, risk_free_rate, std_dev):
        cls.returns = stock_returns
        cls.risk_free_rate = risk_free_rate
        cls.std_dev = std_dev

    def sharpe_ratio(cls):
        return (cls.returns - cls.risk_free_rate) / cls.std_dev
