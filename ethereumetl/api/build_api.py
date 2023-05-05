from ethereumetl.thread_local_proxy import ThreadLocalProxy
from ethereumetl.providers.auto import get_provider_from_uri
from ethereumetl.api.rate_limiting_proxy import RateLimitingProxy


def build_api(provider_uri, rate_limit):
    api = ThreadLocalProxy(lambda: get_provider_from_uri(provider_uri, batch=True))
    if rate_limit is not None and rate_limit > 0:
        api = RateLimitingProxy(api, max_per_second=rate_limit)
    return api