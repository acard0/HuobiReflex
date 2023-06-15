from time import time
from huobi.client.account import AccountClient
from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.utils import *
import time

symbol_test = "rifiusdt"
account_id = "35047541"

trade_client = TradeClient(api_key="227aa823-e34a0596-ur2fg6h2gf-9cd50", secret_key="3f85061a-c2177334-41f0454d-dc02f", url="https://api-aws.huobi.pro")

_loop = True
while _loop:
    try:
        order_id = trade_client.create_order(symbol=symbol_test, account_id=account_id, order_type="buy-limit", source="api", amount=80.0, price=1.2)
        print("order id: " + order_id)
        _loop = False
    except:
        print("failed, retry.") 
    time.sleep(0.030)

