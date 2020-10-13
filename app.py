import logging.handlers,os


def log_conf():
    """初始化日志配置"""
    # 日志文件位置
    logPath = "./log"
    # 日志器
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 处理器 - 控制台
    sh = logging.StreamHandler()
    # 处理器 - 文件
    trfh = logging.handlers.TimedRotatingFileHandler(filename=logPath +os.sep+"mini.log",
                                                     when='midnight',interval=1,
                                                     backupCount=7,encoding="utf_8")
    # 格式化字符串
    f = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    # 格式化器
    formatter = logging.Formatter(f)

    # 处理器添加格式化器
    sh.setFormatter(formatter)
    trfh.setFormatter(formatter)

    # 日志器添加处理器
    logger.addHandler(sh)
    logger.addHandler(trfh)


# 请求通用接口地址
base_url = "http://e.cn/api/v1"

# 微信code
code = "063J510w3xCy7V22sf3w3hdx1p0J510i"

# 请求头
headers = {
    "Content-Type": "application/json",
    "token":"73cf146efa01b82f3538cdd30a9b1e1f"
}