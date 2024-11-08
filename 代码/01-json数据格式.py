import json

# data是一个字符串类型的数据
# json格式的数据 本质上就是字符串
data = """
{
  "discountRate": 1,
  "storeShopNo": "None",
  "dayOrderSeq": 37,
  "storeDistrict": "芙蓉区",
  "isSigned": 0,
  "storeProvince": "湖南省",
  "origin": 0,
  "storeGPSLongitude": "undefined",
  "discount": 0,
  "storeID": 1766,
  "productCount": 1,
  "operatorName": "OperatorName",
  "operator": "NameStr",
  "storeStatus": "open",
  "storeOwnUserTel": 12345678910,
  "payType": "cash",
  "discountType": 2,
  "storeName": "亿户超市郭一一食品店",
  "storeOwnUserName": "OwnUserNameStr",
  "dateTS": 1542436490000,
  "smallChange": 0,
  "storeGPSName": "None",
  "erase": 0,
  "product": [
    {
      "count": 1,
      "name": "南京特醇",
      "unitID": 8,
      "barcode": "6901028300056",
      "pricePer": 12,
      "retailPrice": 12,
      "tradePrice": 11,
      "categoryID": 1
    }
  ],
  "storeGPSAddress": "None",
  "orderID": "154243648991517662217",
  "moneyBeforeWholeDiscount": 12,
  "storeCategory": "normal",
  "receivable": 12,
  "faceID": "",
  "storeOwnUserId": 1694,
  "paymentChannel": 0,
  "paymentScenarios": "OTHER",
  "storeAddress": "StoreAddress",
  "totalNoDiscount": 12,
  "payedTotal": 12,
  "storeGPSLatitude": "undefined",
  "storeCreateDateTS": 1540793134000,
  "storeCity": "长沙市",
  "memberID": "0"
}
"""


# 把json格式数据转化为python数据
python_data = json.loads(data)
# print(type(python_data))
# print(python_data["product"])

# 把python数据转化为json数据
json_data = json.dumps(python_data)
print(type(json_data))
