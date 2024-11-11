"""
零售订单模型
负责构建
- 纯订单相关的数据模型（1比1的class模型）
- 订单和商品相关的数据模型（1比多的class模型）
"""
import json


class OrdersModel:
    """构建订单模型（纯订单，不包含商品信息）"""
    def __init__(self, data: str):
        """
        从传入的字符串数据构建订单model
        此Model只包含订单信息，不包含订单详情（商品售卖）
        """
        # 将一行字符串json转换为字典对象
        data = json.loads(data)

        self.discount_rate = data['discountRate']                   # 折扣率
        self.store_shop_no = data['storeShopNo']                    # 店铺店号（无用列）
        self.day_order_seq = data['dayOrderSeq']                    # 本单为当日第几单
        self.store_district = data['storeDistrict']                 # 店铺所在行政区
        self.is_signed = data['isSigned']                           # 是否签约店铺（签约第三方支付体系）
        self.store_province = data['storeProvince']                 # 店铺所在省份
        self.origin = data['origin']                                # 原始信息（无用）
        self.store_gps_longitude = data['storeGPSLongitude']        # 店铺GPS经度
        self.discount = data['discount']                            # 折扣金额
        self.store_id = data['storeID']                             # 店铺ID
        self.product_count = data['productCount']                   # 本单售卖商品数量
        self.operator_name = data['operatorName']                   # 操作员姓名
        self.operator = data['operator']                            # 操作员ID
        self.store_status = data['storeStatus']                     # 店铺状态
        self.store_own_user_tel = data['storeOwnUserTel']           # 店铺店主电话
        self.pay_type = data['payType']                             # 支付类型
        self.discount_type = data['discountType']                   # 折扣类型
        self.store_name = data['storeName']                         # 店铺名称
        self.store_own_user_name = data['storeOwnUserName']         # 店铺店主名称
        self.date_ts = data['dateTS']                               # 订单时间
        self.small_change = data['smallChange']                     # 找零金额
        self.store_gps_name = data['storeGPSName']                  # 店铺GPS名称
        self.erase = data['erase']                                  # 是否抹零
        self.store_gps_address = data['storeGPSAddress']            # 店铺GPS地址
        self.order_id = data['orderID']                             # 订单ID
        self.money_before_whole_discount = data['moneyBeforeWholeDiscount']  # 折扣前金额
        self.store_category = data['storeCategory']                 # 店铺类别
        self.receivable = data['receivable']                        # 应收金额
        self.face_id = data['faceID']                               # 面部识别ID
        self.store_own_user_id = data['storeOwnUserId']             # 店铺店主ID
        self.payment_channel = data['paymentChannel']               # 付款通道
        self.payment_scenarios = data['paymentScenarios']           # 付款情况（无用）
        self.store_address = data['storeAddress']                   # 店铺地址
        self.total_no_discount = data['totalNoDiscount']            # 整体价格（无折扣）
        self.payed_total = data['payedTotal']                       # 已付款金额
        self.store_gps_latitude = data['storeGPSLatitude']          # 店铺GPS纬度
        self.store_create_date_ts = data['storeCreateDateTS']       # 店铺创建时间
        self.store_city = data['storeCity']                         # 店铺所在城市
        self.member_id = data['memberID']                           # 会员ID
