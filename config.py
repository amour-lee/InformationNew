from redis import StrictRedis


class Config(object):

    # DEBUG = True

    # 配置mysql：指定数据库位置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@mysql@127.0.0.1：3306/information_new'
    # 禁用追踪mysql 因为mysql性能差，如果再去追踪mysql的所有修改 会再次浪费性能
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis 数据库配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 配置秘钥
    SECRET_KEY = 'agshdjfk'

    # 配置Session：：将flask中的session的数据引导到redis
    SESSION_TYPE = 'redis'
    # 配置redis的位置
    SESSION_REDIS = StrictRedis(host = REDIS_HOST,port= REDIS_PORT)
    # 使用签名将Session明文转成密文
    SESSION_USE_SIGNER = True
    # 设置session有效期: 这里指的是session的扩展操作session时设置的有效期 以秒为单位
    PERMANENT_SESSION_LIFETIME = 60 * 60 * 24


class DevelopmentConfig(Config):
    """开发环境配置类
    如果开发环境的配置和父类一样，可以直接pass
    """
    DEBUG = True

class ProductionConfig(Config):
    """生产环境的配置类
    实际开发中，需要额外配置生产环境下的数据库和其他信息
    """
    DEBUG = False

# 工厂方法需要的原材料
configs = {
    'dev':DevelopmentConfig,
    'prod':ProductionConfig
}