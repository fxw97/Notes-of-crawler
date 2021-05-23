# 每次requests请求完之后,要关掉请求：
import requests

resp =requests.get()

resp.close()