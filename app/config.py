from environs import Env

env = Env()
env.read_env()


class Config:
    DEBUG = True
