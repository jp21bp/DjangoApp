from rest_framework.throttling import AnonRateThrottle

class TenCallsPerMin(AnonRateThrottle):
    scope = 'ten'