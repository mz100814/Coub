from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str


    REF_LINK: str = "https://t.me/coub/app?startapp=coub__marker_32227453"



    DELAY_EACH_ACCOUNT: list[int] = [15,25]
    SLEEP_TIME_BETWEEN_EACH_ROUND: list[int] = [18000, 20000]

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()

