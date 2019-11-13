import uuid

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from Book import models
from Book.models import User
from django.views import View

from Book.utils.alipay.alipay import AliPay


class log(View):
    def get(self,request):
        return render(request,'home.html')
    def post(self,request):
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        log_list = models.User.objects.filter(username=user_name)
        pwd = models.User.objects.filter(password=password)
        if log_list and pwd:
            return redirect('/bookhome/')
        else:
            err_msg = '用户名或密码错误'
        return render(request, 'home.html',{'err_msg':err_msg})


class BookHome(View):
    # @login_required
    def get(self,request):
        return render(request,'book_home.html')

class register(View):
    def get(self, request):
        print('0000')
        return render(request,'register.html')

    def post(self,request):
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        username = User.objects.filter(username=user_name)
        if username:
            return HttpResponse("用户名已存在。")
        # models.User.objects.create(name=user_name)
        # models.User.objects.create()

        user = User()
        user.username=user_name
        user.password=password
        user.save()
        return render(request, 'home.html')


#支付宝以下
def shopping(request):
    goods_list = models.BookName.objects.all()

    return render(request, 'zhifubaoshopping.html', {'goods_list': goods_list})
alipay = AliPay(
    appid='2016101700705285',
    app_notify_url='http://47.93.246.49:8081/show_msg/',  # 支付宝发送支付状态信息的地址，支付宝会向这个地址发送post请求，可以先不写但是必须有内容(我这里用的是空格)
    return_url='http://47.93.246.49:8081/show_msg/',  # 将用户浏览器地址重定向回原来的地址，支付宝会向这个地址发送get请求，可以先不写但是必须有内容
    alipay_public_key_path='Book/utils/alipay/zhi_fu_bao_gong_yao.txt',  # 支付宝公钥
    app_private_key_path='Book/utils/alipay/ying_yong_si_yao.txt',  # 应用私钥
    debug=True,  # 默认是True代表测试环境，False代表正式环境
)
def purchase(request,goods_id):
    '''
        订单支付
        :param request:
        :param goods_id:传过来的商品id
        :return:跳转到支付宝支付页面
        '''
    # 获取商品信息，因为向支付宝接口发送请求的时候需要携带该商品相关信息
    obj_books = models.BookName.objects.get(pk=goods_id)  # pk就是商品的标识,等价于使用id
    '''
    生成订单
    '''
    order_number = str(uuid.uuid4())
    # print(order_number)  # bd9ee7fe-aca5-449d-acd1-63bcd8e30cde
    models.BookShoppingOrdering.objects.create(
        order_number=order_number,
        goods=obj_books,  # 或者goods_id=obj_goods.id
    )
    '''
    跳转到支付宝支付页面
    '''
    # 实例化对象
    # alipay = AliPay(
    #     appid='2016101700705285',
    #     app_notify_url=' ',  # 支付宝发送支付状态信息的地址，支付宝会向这个地址发送post请求，可以先不写但是必须有内容(我这里用的是空格)
    #     return_url='http://127.0.0.1:8000/show_msg/',  # 将用户浏览器地址重定向回原来的地址，支付宝会向这个地址发送get请求，可以先不写但是必须有内容
    #     alipay_public_key_path='Book/utils/alipay/zhi_fu_bao_gong_yao.txt',  # 支付宝公钥
    #     app_private_key_path='Book/utils/alipay/ying_yong_si_yao.txt',  # 应用私钥
    #     debug=True,  # 默认是True代表测试环境，False代表正式环境
    # )
    # 定义请求地址传入的参数
    query_params = alipay.direct_pay(
        subject=obj_books.name,  # 商品的简单描述
        out_trade_no=order_number,  # 商品订单号
        total_amount=111,  # 交易金额(单位是元，保留两位小数)
    )
    # 需要跳转到支付宝的支付页面，所以需要生成跳转的url
    pay_url = 'https://openapi.alipaydev.com/gateway.do?{0}'.format(query_params)
    return redirect(pay_url)


def show_msg(request):
    # alipay = AliPay(
    #     appid="2016101700705285",  # APPID
    #     app_notify_url='http://47.93.246.49:8000/show_msg/',  # 支付宝发送支付状态信息的地址，支付宝会向这个地址发送post请求，可以先不写但是必须有内容
    #     return_url='http://127.0.0.1:8000/show_msg/',  # 将用户浏览器地址重定向回原来的地址，支付宝会向这个地址发送get请求，可以先不写但是必须有内容
    #     app_private_key_path='Book/utils/alipay/ying_yong_si_yao.txt',  # 应用私钥
    #     alipay_public_key_path='Book/utils/alipay/zhi_fu_bao_gong_yao.txt',  # 支付宝公钥
    #     debug=True,  # 默认是False
    # )
    if request.method == 'GET':
        # alipay = AliPay(
        #     appid="2016101700705285",  # APPID
        #     app_notify_url='http://127.0.0.1:8000/check_order/',  # 支付宝发送支付状态信息的地址，支付宝会向这个地址发送post请求，可以先不写但是必须有内容
        #     return_url='http://127.0.0.1:8000/show_msg/',  # 将用户浏览器地址重定向回原来的地址，支付宝会向这个地址发送get请求，可以先不写但是必须有内容
        #     app_private_key_path='Book/utils/alipay/ying_yong_si_yao.txt',  # 应用私钥
        #     alipay_public_key_path='Book/utils/alipay/zhi_fu_bao_gong_yao.txt',  # 支付宝公钥
        #     debug=True,  # 默认是False
        # )
        params = request.GET.dict()  # 获取请求携带的参数并转换成字典类型
        print(request.GET)  # <QueryDict: {'charset': ['utf-8'], 'out_trade_no': ['04f09b6f-e792-4a1d-8dbc-c68f1d046622'], ……}
        print(params)  # {'charset': 'utf-8', 'out_trade_no': '04f09b6f-e792-4a1d-8dbc-c68f1d046622',……}
        sign = params.pop('sign', None)  # 获取sign的值
        # 对sign参数进行验证
        status = alipay.verify(params, sign)
        if status:
            return render(request, 'show_msg.html', {'msg': '支付成功'})
        else:
            return render(request, 'show_msg.html', {'msg': '支付失败'})
    # else:
    #     return render(request, 'show_msg.html', {'msg': '只支持GET请求，不支持其它请求'})
    if request.method == 'POST':
        # alipay = AliPay(
        #     appid="2016101200668044",  # APPID
        #     app_notify_url='http://192.168.1.148:8000/check_order/',  # 支付宝会向这个地址发送post请求
        #     return_url='http://127.0.0.1:8000/show_msg/',  # 支付宝会向这个地址发送get请求
        #     app_private_key_path='Book/utils/alipay/ying_yong_si_yao.txt',  # 应用私钥
        #     alipay_public_key_path='Book/utils/alipay/zhi_fu_bao_gong_yao.txt',  # 支付宝公钥
        #     debug=True,
        # )
        print('request.body：', request.body)  # 是字节类型,b'gmt_create=2019-09-21+17%3A00%3A15&charset=utf-8&……
        body_str = request.body.decode('utf-8')  # 转成字符串
        # print('body_str：', body_str)
        from urllib.parse import parse_qs
        post_data = parse_qs(body_str)  # 根据&符号分割
        print(post_data)  # post_data是一个字符串
        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]
        sign = post_dict.pop('sign', None)
        status = alipay.verify(post_dict, sign)
        if status:  # 支付成功
            out_trade_no = post_data['out_trade_no']
            models.BookShoppingOrdering.objects.filter(order_number=out_trade_no).update(order_status=1)
            return HttpResponse('success')  # 向支付宝返回success,表示接收到请求
        else:
            return HttpResponse('支付失败')

# def check_order(request):
#     '''
#     支付宝通知支付的结果信息，如果支付成功可以用来修改订单的状态
#     :param request:
#     :return:
#     '''
#     if request.method == 'POST':
#         alipay = AliPay(
#             appid="2016101200668044",  # APPID
#             app_notify_url='http://192.168.1.148:8000/check_order/',  # 支付宝会向这个地址发送post请求
#             return_url='http://127.0.0.1:8000/show_msg/',  # 支付宝会向这个地址发送get请求
#             app_private_key_path='Book/utils/alipay/ying_yong_si_yao.txt',  # 应用私钥
#             alipay_public_key_path='Book/utils/alipay/zhi_fu_bao_gong_yao.txt',  # 支付宝公钥
#             debug=True,
#         )
#         print('request.body：', request.body)  # 是字节类型,b'gmt_create=2019-09-21+17%3A00%3A15&charset=utf-8&……
#         body_str = request.body.decode('utf-8')  # 转成字符串
#         # print('body_str：', body_str)
#         from urllib.parse import parse_qs
#         post_data = parse_qs(body_str)  # 根据&符号分割
#         print(post_data)  # post_data是一个字符串
#         post_dict = {}
#         for k, v in post_data.items():
#             post_dict[k] = v[0]
#         sign = post_dict.pop('sign', None)
#         status = alipay.verify(post_dict, sign)
#         if status:  # 支付成功
#             out_trade_no = post_data['out_trade_no']
#             models.BookShoppingOrdering.objects.filter(order_number=out_trade_no).update(order_status=1)
#             return HttpResponse('success')  # 向支付宝返回success,表示接收到请求
#         else:
#             return HttpResponse('支付失败')
#     else:
#         return HttpResponse('只支持POST请求')