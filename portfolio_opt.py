import riskfolio.Portfolio as pf

def optimize_portfolio(returns):
    port = pf.Portfolio(returns=returns)
    port.assets_stats(method_mu='hist', method_cov='hist')
    model = 'Classic'
    rm = 'MV'
    obj = 'Sharpe'
    weights = port.optimization(model=model, rm=rm, obj=obj, rf=0.02)
    return weights
